from django.shortcuts import render
from . models import *


# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def news(request):
    # all_news = News.objects.order_by('-date_added')
    # context = {'news': all_news}

    return render(request, 'main/news.html')


def schedule(request):
    return render(request, 'main/schedule.html')


def about(request):
    return render(request, 'main/about.html')


def teacher(request):
    return render(request, 'main/teacher.html')


def modules(request):
    # all_modules = Module.objects.order_by('title')

    # context = {'modules': all_modules'}

    return render(request, 'main/modules.html')


def certificate(request):
    return render(request, 'main/certificate.html')


def content(request):
    return render(request, 'main/content.html')
