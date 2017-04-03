from django.shortcuts import render
from data import posts


def index(request):
    context = {'posts': posts}
    return render(request, 'index.html', context)