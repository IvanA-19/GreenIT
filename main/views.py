from django.shortcuts import render
from . models import *
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'main/index.html')


@login_required(login_url='users:login')
def schedule(request):
    return render(request, 'main/schedule.html')


def about(request):
    return render(request, 'main/about.html')


def teacher(request):
    return render(request, 'main/teacher.html')


@login_required(login_url='users:login')
def modules(request):
    all_modules = Module.objects.order_by('title')

    context = {'modules': all_modules}

    return render(request, 'main/modules.html', context)


@login_required(login_url='users:login')
def module_view(request, module_slug):
    current_module = Module.objects.get(module_slug=module_slug)
    topics = Topic.objects.prefetch_related('module').filter(module=current_module)
    context = {'module': current_module, 'topics': topics}

    return render(request, 'main/module.html', context)


@login_required(login_url='users:login')
def topic_view(request, topic_slug):
    current_topic = Topic.objects.get(topic_slug=topic_slug)
    subtopics = Subtopic.objects.prefetch_related('topic').filter(topic=current_topic)

    context = {'topic': current_topic, 'subtopics': subtopics}

    return render(request, 'main/topic.html', context)


