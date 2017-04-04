from django.shortcuts import render, get_object_or_404
from .models import Post


def index(request):
    posts = Post.objects.all().order_by('-posted_date')
    context = {'posts': posts,
               'specific_post': False}
    return render(request, 'index.html', context)


def post(request, slug):
    single_post = get_object_or_404(Post, slug=slug)
    context = {'posts': [single_post],
               'specific_post': True}
    return render(request, 'index.html', context)
