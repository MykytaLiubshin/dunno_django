from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author_name = models.CharField(max_length=200)
    content = models.CharField(max_length=1000)
    creation_date = models.DateTimeField(default = timezone.now)
