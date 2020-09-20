from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from import_export.admin import ImportExportModelAdmin

from core.admin import BaseAdmin
from .models import Currency
from .resources import CurrencyResource


@admin.register(Currency)
class CurrencyAdmin(BaseAdmin, ImportExportModelAdmin):
    """"""
    resource_class = CurrencyResource
