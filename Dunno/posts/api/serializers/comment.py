from rest_framework import serializers
from posts.models import Comment, Post
from django.shortcuts import get_object_or_404
from django.http import HttpResponse



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'id',
            'author_name',
            'content',
            'creation_date',
            'post_id'
        )
    
    def create(self, validated_data):
        inst = Comment(**validated_data)
        inst.save()
        print(inst)
        parent = Post.objects.filter(id=inst.post_id)
        print(parent)
        if len(parent) != 0:
            ch = parent[0].children
            ch.append(inst.id)
            parent.update(children=ch)

            return inst
        else:
            return None
        return inst
    