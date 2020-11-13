from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse
from posts.models import Post
from posts.utils import flush_posts


# Create your views here.
def upvote_a_post(request, identificator):
    post = Post.objects.filter(id=identificator)
    if len(post) != 0:
        post.update(upvotes=post[0].upvotes + 1)
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=404)


def redirect_post_link(request, identificator):
    post = get_object_or_404(Post, id=identificator)
    if post:
        return redirect(post.link)
    else:
        return HttpResponse(status=404)
