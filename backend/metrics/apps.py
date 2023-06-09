from django.apps import AppConfig


class MetricsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'metrics'
    verbose_name = 'Метрики'

    def ready(self):
        from .signals import handlers  # noqa
