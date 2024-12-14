from __future__ import absolute_import, unicode_literals
from celery.schedules import crontab
import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news_website.settings')

app = Celery('news_website')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
