from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from posts.api.serializers.post import PostSerializer
from posts.models import Post, Comment


class ListPosts(APIView):
    def get(self, request, format=None, identificator=None):
        if identificator is not None:
            posts = Post.objects.filter(id=identificator)
        else:
            posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def patch(self, request, *args, **kwargs):
        post = get_object_or_404(
            Post, identificator=kwargs["identificator"]
        )
        serializer = PostSerializer(
            post, data=request.data, partial=True
        )
        if serializer.is_valid():
            post = serializer.save()
            return Response(PostSerializer(post).data)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, identificator):
        post = get_object_or_404(Post, id=identificator)
        children = post.children

        for child in children:
            Comment.objects.filter(id=child).delete()

        post.delete()
        return Response(f"Post {identificator} deleted successfully")
