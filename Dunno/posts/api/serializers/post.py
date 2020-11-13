from rest_framework import serializers
from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "title",
            "link",
            "creation_date",
            "upvotes",
            "author_name",
        )

    def post(self, data):
        instance = Post.objects.create(**data)
        return instance
