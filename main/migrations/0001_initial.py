# Generated by Django 5.0.2 on 2024-02-26 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Модуль')),
                ('enabled', models.BooleanField(verbose_name='Доступен')),
            ],
        ),
    ]
