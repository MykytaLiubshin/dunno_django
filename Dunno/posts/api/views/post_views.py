from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from posts.models import Post
from posts.api.serializers.post import PostSerializer


class PostListCreateAPIView(ListCreateAPIView):
    """
    API view to retrieve list of posts or create new
    """

    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostDetailsAPIView(RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update or delete post
    """

    serializer_class = PostSerializer
    queryset = Post.objects.all()
