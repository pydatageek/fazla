from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class LinguisticsConfig(AppConfig):
    name = 'linguistics'
    verbose_name = _('Linguistics')
