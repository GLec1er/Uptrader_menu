from django.shortcuts import render
from django.shortcuts import get_object_or_404
from . models import MenuItem


def pages(request, url):
    return render(request, 'pages.html')
