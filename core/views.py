from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from . import models
from . import forms


# Create your views here.
def home(request):
    return redirect('post_list', category_slug='blog')


def post_list(request, category_slug):
    if category_slug in models.Post.CATEGORIES:
        return render(request, 'core/post_list.html', {
            'posts': models.Post.published_objects.filter(category=category_slug).order_by('published_at'),
        })
    elif category_slug in models.HTMLPost.CATEGORIES:
        pass

    raise ValueError("This category doesn't exist")


def post_detail(request, category_slug, post_slug):
    if category_slug in models.HTMLPost.CATEGORIES:
        model = models.HTMLPost
    else:
        model = models.Post

    post = get_object_or_404(model, category=category_slug, slug=post_slug)

    return render(request, 'core/post.html', {
        'post': post,
        'comment_form': forms.CommentForm(),
    })


def comment(request, category_slug, post_slug):
    if category_slug in models.HTMLPost.CATEGORIES:
        model = models.HTMLPost
    else:
        model = models.Post

    post = get_object_or_404(model, category=category_slug, slug=post_slug)

    comment_obj = models.Comment(
        author=request.POST['author'],
        text=request.POST['text'],
    )

    post.comments.add(comment_obj, bulk=False)

    return redirect(post.get_absolute_url())


def about(request):
    return render(request, 'core/about.html', {})
