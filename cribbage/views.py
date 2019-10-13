from django.shortcuts import render

from django.http import HttpResponseNotFound
from django.template.exceptions import TemplateDoesNotExist


def cribbage_detail(request, slug):
    try:
        return render(request, f'cribbage/posts/{slug}.html', {})
    except TemplateDoesNotExist:
        return HttpResponseNotFound()


def cribbage_home(request):
    return render(request, 'cribbage/cribbage.html', {})
