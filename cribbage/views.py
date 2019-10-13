from django.shortcuts import render
from django.shortcuts import get_object_or_404

from . import models


def cribbage_detail(request, slug):
    cribbage = get_object_or_404(models.CribbagePost, slug=slug)

    return render(request, 'core/post.html', {
        'post': cribbage,
    })


def cribbage_home(request):
    return render(request, 'cribbage/cribbage.html', {})
