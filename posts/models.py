from __future__ import unicode_literals

from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify


class Post(models.Model):
    title = models.CharField(max_length=200, blank=False)
    content = MarkdownxField()
    image = models.ImageField(blank=True)
    posted_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)

    @property
    def markdown(self):
        return markdownify(self.content)

    @models.permalink
    def get_absolute_url(self):
        return 'blog:post', (self.slug,)

    def __str__(self):
        return self.title
