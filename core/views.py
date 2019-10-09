from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from . import models


# Create your views here.
def home(request):
    return redirect('blog')


def blog_post_list(request):
    posts = models.BlogPost.objects.all()

    return render(request, 'core/post_list.html', {
        'posts': posts,
    })


def stories_list(request):
    stories = models.Story.objects.all()

    return render(request, 'core/post_list.html', {
        'posts': stories,
    })


def blog_post_detail(request, slug):
    blog_post = get_object_or_404(models.BlogPost, slug=slug)

    return render(request, 'core/post.html', {
        'post': blog_post,
    })


def story_detail(request, slug):
    story = get_object_or_404(models.Story, slug=slug)

    return render(request, 'core/post.html', {
        'post': story,
    })


def about(request):
    return render(request, 'core/about.html', {})
