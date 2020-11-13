from rest_framework import serializers
from posts.models import Comment, Post
from django.shortcuts import get_object_or_404
from django.http import HttpResponse


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("id", "author_name", "content", "creation_date", "post_id")
