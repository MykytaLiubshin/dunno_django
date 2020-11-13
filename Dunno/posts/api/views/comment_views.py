from rest_framework.views import APIView
from rest_framework.response import Response

from posts.models import Comment, Post
from posts.api.serializers.comment import CommentSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404


class ListComments(APIView):
    def get(self, request, format=None, pk=None, post=None):
        if pk is not None:
            comments = Comment.objects.filter(id=pk)
        elif post is not None:
            comments = Comment.objects.filter(post_id=post)
        else:
            comments = Comment.objects.all()

        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            parent = Post.objects.filter(id=serializer.data["post_id"])
            if len(parent) == 0:
                return Response(
                    "This post does not exist. You cannot comment it.",
                    status=status.HTTP_400_BAD_REQUEST,
                )

            _ch = parent[0].children
            _ch.append(serializer.data["id"])
            parent.update(children=_ch)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        comment = get_object_or_404(Comment, pk=kwargs["pk"])
        serializer = CommentSerializer(
            comment, data=request.data, partial=True
        )
        if serializer.is_valid():
            comment = serializer.save()
            return Response(CommentSerializer(comment).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        comment = get_object_or_404(Comment, id=pk)
        parent = Post.objects.filter(id=comment.post_id)
        print(parent)
        _ch = parent[0].children
        _ch = list(filter(lambda ind: ind != comment.id, _ch))
        parent.update(children=_ch)
        comment.delete()
        return Response(f"Comment {pk} deleted successfully")
