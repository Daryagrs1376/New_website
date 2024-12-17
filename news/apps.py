from django.apps import AppConfig
from haystack import connections
from haystack.management.commands import update_index

class NewsConfig(AppConfig):
    name = 'news'

    def ready(self):
        from haystack.management.commands.update_index import Command
        Command().handle()  # این متد به روزرسانی ایندکس‌ها را انجام می‌دهد
