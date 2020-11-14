from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField

"""
This file has models for Django ORM:
    - Post
    - Comment
"""

BASE_LENGTH = 200

# Class Post that extends Djangos model
# Represents a real post.
# @prop title           - The title of the post
#  - String
# @prop link            - The link to the post
#  - String
# @prop creation_date   - The time and date of the creation of the post
#  - DateTime type
# @prop upvotes         - The upvotes of the post
#  - Integer
# @prop author_name     - The name of the author of the post
#  - String
# @prop children        - A list of ids of the comments to this post
#  - List of Integers


class Post(models.Model):
    title = models.CharField(max_length=BASE_LENGTH)
    link = models.CharField(max_length=BASE_LENGTH)
    creation_date = models.DateTimeField(default=timezone.now)
    upvotes = models.IntegerField(default=0)
    author_name = models.CharField(max_length=BASE_LENGTH)
    children = ArrayField(
        models.IntegerField(blank=True), blank=True, default=list
    )
    # An underscore function to print out an element
    # in the console. Used for debugging mostly

    def __str__(self) -> str:
        return f"""
        title = {self.title},
        link = {self.link},
        upvotes = {self.upvotes}
        """


# Class Post that extends Djangos model
# Represents a real post.
# @prop author_name     - The name of the author of the comment
# - String
# @prop creation_date   - The time and date of the creation of the comment
# - DateTime type
# @prop content         - The content of the comment
# - String
# @prop post_id         - The id of the parent post
# - Integer
class Comment(models.Model):
    author_name = models.CharField(max_length=BASE_LENGTH)
    content = models.CharField(max_length=BASE_LENGTH * 5)
    creation_date = models.DateTimeField(default=timezone.now)
    post_id = models.IntegerField()

    # An underscore function to print out an element
    # in the console. Used for debugging mostly
    def __str__(self) -> str:
        return f"""
        author_name = {self.author_name},
        content = {self.content},
        post_id = {self.post_id}"""
