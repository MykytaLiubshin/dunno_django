from posts.models import Post


def flush_posts():
    Post.objects.all().update(upvotes=0)
    print("All upvotes are flushed.")
