# Generated by Django 4.2.14 on 2024-11-25 22:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_article_deleted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='deleted',
        ),
    ]
