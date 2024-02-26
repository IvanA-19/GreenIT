from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('news/', views.news, name='news'),
    path('schedule/', views.schedule, name='schedule'),
    path('about/', views.about, name='about'),
    path('certificate/', views.certificate, name='certificate'),
    path('teacher/', views.teacher, name='teacher'),
    path('modules', views.modules, name='modules'),
    path('content/', views.content, name='content')

]
