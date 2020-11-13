from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from posts.models import Comment
from posts.api.serializers.comment import CommentSerializer


class CommentListCreateAPIView(ListCreateAPIView):
    """
    API view to retrieve list of Comments or create new
    """

    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class CommentDetailsAPIView(RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update or delete Comment
    """

    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
