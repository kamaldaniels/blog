from __future__ import unicode_literals

import logging

from google.appengine.api import memcache

from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify

POSTS_CACHE_KEY = 'posts'


class Post(models.Model):
    title = models.CharField(max_length=200, blank=False)
    content = MarkdownxField()
    image = models.ImageField(blank=True)
    posted_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        memcache.delete(POSTS_CACHE_KEY)
        super(Post, self).save(*args, **kwargs)

    @property
    def markdown(self):
        return markdownify(self.content)

    @models.permalink
    def get_absolute_url(self):
        return 'blog:post', (self.slug,)

    def __str__(self):
        return self.title


def get_posts():
    posts = memcache.get(POSTS_CACHE_KEY)
    if posts is not None:
        return posts
    else:
        logging.info('Getting posts from datastore...')
        posts = Post.objects.all().order_by('-posted_date')
        memcache.add(POSTS_CACHE_KEY, posts)
    return posts