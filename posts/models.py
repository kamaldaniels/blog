from __future__ import unicode_literals

from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200, blank=False)
    content = models.TextField()
    image = models.ImageField(blank=True)
    posted_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)

    @models.permalink
    def get_absolute_url(self):
        return 'blog:post', (self.slug,)

    def __str__(self):
        return self.title
