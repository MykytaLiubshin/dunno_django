from rest_framework import serializers

from posts.models import Post


# Class PostSerializer extends
# django_rest_framework serializers model
# Is a serializer for Post objects
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "link",
            "creation_date",
            "upvotes",
            "author_name",
            "children",
        )
