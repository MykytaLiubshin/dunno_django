from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def upvote_a_post(request, identificator):
    
    obj = Post.objects.filter(id=identificator)
    obj.update(upvotes=obj[0].upvotes + 1)
    print("="*50)
    print(obj[0].upvotes)
    print("="*50)

    
    return render()

