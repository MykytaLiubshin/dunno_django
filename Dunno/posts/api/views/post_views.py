from rest_framework.views import APIView
from rest_framework.response import Response

from posts.models import Post
from posts.api.serializers.post import PostSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404


class ListPosts(APIView):
    def get(self, request, format=None, pk=None):
        if pk is not None:
            posts = Post.objects.filter(id=pk)
        else:
            posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs["pk"])
        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            post = serializer.save()
            return Response(PostSerializer(post).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        post = get_object_or_404(Post, id=pk)
        post.delete()
        return Response(f"Post {pk} deleted successfully")
