# Generated by Django 5.0.2 on 2024-03-03 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_useranswer_task_useranswer_topic_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='News',
        ),
    ]