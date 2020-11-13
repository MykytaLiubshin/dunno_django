from posts.models import Post
from time import sleep
from threading import Thread

FLUSH_INTERVAL = 60 * 60 * 24


def bg(fn, interval=FLUSH_INTERVAL, *args, **kwargs):
    r = Thread(target=fn, args=([interval]), daemon=True)
    r.start()


def task(interval):
    while True:
        Post.objects.all().update(upvotes=0)
        print("All upvotes are flushed.")
        sleep(interval)
