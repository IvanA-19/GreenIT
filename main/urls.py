from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('schedule/', views.schedule, name='schedule'),
    path('about/', views.about, name='about'),
    path('teacher/', views.teacher, name='teacher'),
    path('modules', views.modules, name='modules'),
    path('modules/<slug:module_slug>', views.module_view, name='module'),
    path('topics/<slug:topic_slug>', views.topic_view, name='topic'),

]
