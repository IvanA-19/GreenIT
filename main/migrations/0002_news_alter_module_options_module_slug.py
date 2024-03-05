# Generated by Django 5.0.2 on 2024-02-26 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Новость')),
                ('content', models.TextField(verbose_name='Текст')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='media/news', verbose_name='Фото')),
                ('date_added', models.DateTimeField(auto_now=True, verbose_name='Дата добавления')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
        ),
        migrations.AlterModelOptions(
            name='module.js',
            options={'verbose_name': 'Модуль', 'verbose_name_plural': 'Модули'},
        ),
        migrations.AddField(
            model_name='module.js',
            name='slug',
            field=models.SlugField(default='Module 1', max_length=255, unique=True, verbose_name='URL'),
            preserve_default=False,
        ),
    ]
