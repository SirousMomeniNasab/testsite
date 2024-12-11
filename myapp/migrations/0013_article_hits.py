# Generated by Django 4.2.14 on 2024-09-20 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_remove_article_hits'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='hits',
            field=models.ManyToManyField(blank=True, related_name='hits', through='myapp.ArticleHit', to='myapp.ipaddress', verbose_name='بازدیدها'),
        ),
    ]
