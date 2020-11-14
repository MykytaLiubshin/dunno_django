from rest_framework import serializers

from posts.models import Comment


# Class CommentSerializer extends
# django_rest_framework serializers model
# Is a serializer for Comment objects
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            "id",
            "author_name",
            "content",
            "creation_date",
            "post_id",
        )
