from django.db import models


# Create your models here.
class Module(models.Model):
    title = models.CharField(max_length=300, verbose_name='Модуль')
    enabled = models.BooleanField(verbose_name='Доступен')
    description = models.TextField(verbose_name='Описание', null=True)
    module_slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/modules/{self.module_slug}'

    class Meta:
        verbose_name = 'Модуль'
        verbose_name_plural = 'Модули'
        ordering = ['title', 'id']


class Topic(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, verbose_name='Модуль')
    title = models.CharField(max_length=300, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    home_tasks = models.TextField(verbose_name='Домашние задачи', null=True, blank=True)
    link = models.CharField(max_length=500, verbose_name='Ссылка на google-форму для ответов', null=True, blank=True)
    video = models.CharField(max_length=300, null=True, blank=True, verbose_name='Запись занятия')
    topic_slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'topics/{self.topic_slug}/'

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'
        ordering = ['title', 'id']


class Subtopic(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, verbose_name='Тема')
    title = models.CharField(max_length=300, verbose_name='Название')
    content = models.TextField(verbose_name='Содержание', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Подтема'
        verbose_name_plural = 'Поддемы'
        ordering = ['topic', 'id']
