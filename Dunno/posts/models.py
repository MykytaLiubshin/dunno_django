from django.db import models
from django.utils import timezone


# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    creation_date = models.DateTimeField(default=timezone.now)
    upvotes = models.IntegerField(default=0)
    author_name = models.CharField(max_length=200)

    def __str__(self):
        return f"""
        title = {self.title},
        link = {self.link},
        upvotes = {self.upvotes}
        """


class Comment(models.Model):
    author_name = models.CharField(max_length=200)
    content = models.CharField(max_length=400)
    creation_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"author_name = {self.author_name},content = {self.content}"
