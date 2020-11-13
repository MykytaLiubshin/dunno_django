from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse
from posts.models import Post

# TYPES IMPORTS
from django.core.handlers.wsgi import WSGIRequest


# Calling a bg task
from posts.task import bg, task

bg(task)


# Simple functional views with separate endpoints

# View to work with an endpoint to upvote a post
# upvote_a_post
def upvote_a_post(
    request: WSGIRequest, identificator: int
) -> HttpResponse:
    post = Post.objects.filter(id=identificator)
    if len(post) != 0:
        post.update(upvotes=post[0].upvotes + 1)
        return HttpResponse(status=200)

    else:
        return HttpResponse(status=404)


# View to work with a redirection to the soutce
# redirect_post_link
def redirect_post_link(
    request: WSGIRequest, identificator: int
) -> HttpResponse:
    post = get_object_or_404(Post, id=identificator)

    if post:
        return redirect(post.link)
    else:
        return HttpResponse(status=404)
