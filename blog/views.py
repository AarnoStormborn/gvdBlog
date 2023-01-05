from django.shortcuts import render
from .models import BlogPost


def index(request):
    return render(request, 'index.html')


def blogList(request):
    blogs = BlogPost.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, 'blogList.html', context)


def blogDetail(request, pk, slug):
    blog = BlogPost.objects.get(id=pk)
    context = {
        'blog': blog
    }
    return render(request, 'blogPost.html', context)
