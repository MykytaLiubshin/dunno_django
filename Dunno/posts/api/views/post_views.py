from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# TYPES IMPORTS
from django.core.handlers.wsgi import WSGIRequest
from typing import Optional, Union

from posts.api.serializers.post import PostSerializer
from posts.models import Post, Comment


# Class ListPosts extends django_rest_framework APIView.
# Is a simple implementation of a CRUD API View
# Each request method of CRUD has a corresponding function
# which makes the whole APIView easily customizable
class ListPosts(APIView):
    def get(
        self,
        request: WSGIRequest,
        identificator: Optional[Union[str, int]] = None,
    ) -> Response:
        if identificator is not None:
            posts = Post.objects.filter(id=identificator)
        else:
            posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request: WSGIRequest) -> Response:
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
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
            return Response("You did not specify the post.", status=404)
        post = get_object_or_404(Post, id=identificator)
        serializer = PostSerializer(
            post, data=request.data, partial=True
        )
        if serializer.is_valid():
            post = serializer.save()
            return Response(PostSerializer(post).data)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(
        self,
        request: WSGIRequest,
        identificator: Optional[Union[str, int]] = None,
    ) -> Response:
        if identificator is None:
            return Response("You did not specify the post.", status=404)
        post = get_object_or_404(Post, id=identificator)
        children = post.children

        for child in children:
            Comment.objects.filter(id=child).delete()

        post.delete()
        return Response(f"Post {identificator} deleted successfully")
