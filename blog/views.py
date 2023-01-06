from django.shortcuts import render, redirect
from django.contrib import messages
from .models import BlogPost, BlogComment
from .forms import BlogCommentForm


def index(request):
    return render(request, 'index.html')


def blogList(request):
    blogs = BlogPost.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, 'blogList.html', context)


def blogDetail(request, slug, pk):
    form = BlogCommentForm()
    blog = BlogPost.objects.get(id=pk)
    comments = BlogComment.objects.filter(blog=pk, show_comment=True)
    context = {
        'blog': blog,
        'comments': comments,
        'form': form
    }
    if request.method == 'POST':
        form = BlogCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.save()
            return redirect('blogDetail', slug, pk)
    return render(request, 'blogPost.html', context)
