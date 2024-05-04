from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AirticlesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core_apps.articles"
    verbose_name = _('Airticles')

    def ready(self):
        import core_apps.search.signals
