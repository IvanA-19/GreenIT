from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Module(models.Model):
    title = models.CharField(max_length=300, verbose_name='Модуль')
    enabled = models.BooleanField(verbose_name='Доступен')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    class Meta:
        verbose_name = 'Модуль'
        verbose_name_plural = 'Модули'


class News(models.Model):
    title = models.CharField(max_length=300, verbose_name='Новость')
    content = models.TextField(verbose_name='Текст')
    photo = models.ImageField(upload_to='media/news', blank=True, null=True, verbose_name='Фото')
    date_added = models.DateTimeField(auto_now=True, verbose_name='Дата добавления')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Topic(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    title = models.CharField(max_length=300, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'


class SubTopic(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    title = models.CharField(max_length=300, verbose_name='Название')
    content = models.TextField(verbose_name='Содержание')
    video = models.FileField(upload_to='media/video', null=True, blank=True, verbose_name='Запись занятия')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    class Meta:
        verbose_name = 'Под-тема'
        verbose_name_plural = 'Под-темы'


class Tasks(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    content = models.TextField(verbose_name='Текст задач')
    enabled = models.BooleanField(verbose_name='Задания доступны для выполнения')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    class Meta:
        verbose_name_plural = 'Задачи'
        verbose_name = 'Задачи'


class UserAnswer(models.Model):
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.TextField(verbose_name='Ссылка на git')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    class Meta:
        verbose_name_plural = 'Ответы пользователей'
