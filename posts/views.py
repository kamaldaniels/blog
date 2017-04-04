from django.shortcuts import render
from .models import Post


def index(request):
    posts = Post.objects.all().order_by('-posted_date')
    context = {'posts': posts}
    return render(request, 'index.html', context)
