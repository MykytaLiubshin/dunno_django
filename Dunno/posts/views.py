from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse
from .models import Post


# Create your views here.
def upvote_a_post(request, identificator):
    obj = Post.objects.filter(id=identificator)
    if len(obj) != 0:
        obj.update(upvotes=obj[0].upvotes + 1)
        print("=" * 50)
        print(obj[0].upvotes)
        print("=" * 50)
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=404)


def redirect_post_link(request, identificator):
    post = get_object_or_404(Post, id=identificator)
    if post:
        return redirect(post.link)
    else:
        return HttpResponse(status=404)
