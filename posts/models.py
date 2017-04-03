from __future__ import unicode_literals

from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200, blank=False)
    content = models.TextField()
    image = models.ImageField()
    posted_date = models.DateTimeField(auto_now_add=True)
