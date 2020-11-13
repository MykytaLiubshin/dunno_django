from posts.models import Post
from time import sleep
from threading import Thread
from typing import Callable
#Constants
FLUSH_INTERVAL: int = 60 * 60 * 24

# bg - a function to wrap a task function into an execution thread
def bg(fn: Callable, interval:int = FLUSH_INTERVAL, *args, **kwargs):
    r = Thread(target=fn, args=([interval]), daemon=True)
    r.start()

# task - a function to do one certain task
# to reset (flush) all the upvotes once a day
# might rewrite later
def task(interval: int) -> None:
    while True:
        Post.objects.all().update(upvotes=0)
        print("All upvotes are flushed.")
        sleep(interval)
