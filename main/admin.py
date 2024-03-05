from django.contrib import admin
from .models import *


# Register your models here.
class ModuleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'enabled']
    list_display_links = ['id', 'title', 'enabled']
    search_fields = ['title']
    prepopulated_fields = {"module_slug": ("title",)}


class TopicAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
    search_fields = ['title']
    prepopulated_fields = {"topic_slug": ("title",)}


class SubtopicAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'topic']
    list_display_links = ['id', 'title', 'topic']
    search_fields = ['title', 'topic']


admin.site.register(Module, ModuleAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Subtopic, SubtopicAdmin)
