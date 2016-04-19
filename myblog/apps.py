from django.apps import AppConfig


class MyblogConfig(AppConfig):
    name = 'myblog'

    def ready(self):
        from . import defaults
