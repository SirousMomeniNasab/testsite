# Generated by Django 4.2.14 on 2024-09-20 23:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_articlehit_article_hits'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='hits',
        ),
    ]