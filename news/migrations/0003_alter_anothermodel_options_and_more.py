# Generated by Django 5.1.3 on 2024-12-31 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_remove_newsarticle_created_at_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='anothermodel',
            options={'verbose_name': 'Another Model', 'verbose_name_plural': 'Another Models'},
        ),
        migrations.AlterModelOptions(
            name='newskeywords',
            options={'verbose_name': 'News Keyword', 'verbose_name_plural': 'News Keywords'},
        ),
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='dislikes',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='news',
        ),
    ]
