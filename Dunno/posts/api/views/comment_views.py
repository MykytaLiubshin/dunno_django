from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.handlers.wsgi import WSGIRequest
from typing import Optional, Union

from posts.models import Comment, Post
from posts.api.serializers.comment import CommentSerializer


# Class ListComments extends django_rest_framework APIView.
# Is a simple implementation of a CRUD API View
class ListComments(APIView):
    def get(
        self,
        request: WSGIRequest,
        identificator: Optional[Union[str, int]] = None,
        post=None,
    ) -> Response:
        if identificator is not None:
            comments = Comment.objects.filter(id=identificator)
        elif post is not None:
            comments = Comment.objects.filter(post_id=post)
        else:
            comments = Comment.objects.all()

        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request: WSGIRequest) -> Response:
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            parent = Post.objects.filter(id=serializer.data["post_id"])
            if len(parent) == 0:
                return Response(
                    "This post does not exist. You cannot comment it.",
                    status=status.HTTP_400_BAD_REQUEST,
                )
            # Adding a child to the parent Post object

            _ch = parent[0].children
            _ch.append(serializer.data["id"])
            parent.update(children=_ch)

            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def patch(
        self,
        request: WSGIRequest,
        identificator: Optional[Union[str, int]] = None,
    ) -> Response:
        if identificator is None:
            return Response(
                "You did not specify the comment.", status=404
            )

        comment = get_object_or_404(Comment, id=identificator)
        serializer = CommentSerializer(
            comment, data=request.data, partial=True
        )
        if serializer.is_valid():
            comment = serializer.save()
            return Response(CommentSerializer(comment).data)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(
        self,
        request: WSGIRequest,
        identificator: Optional[Union[str, int]] = None,
    ) -> Response:
        if identificator is None:
            return Response(
                "You did not specify the comment.", status=404
            )
        comment = get_object_or_404(Comment, id=identificator)
        parent = Post.objects.filter(id=comment.post_id)
        # Removing a child comment from the parent Post object

        _ch = parent[0].children
        _ch = list(filter(lambda ind: ind != comment.id, _ch))

        parent.update(children=_ch)
        comment.delete()
        return Response(f"Comment {identificator} deleted successfully")
