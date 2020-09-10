from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from import_export.admin import ImportExportModelAdmin

from core.admin import BaseAdmin
from .models import Info
from .resources import InfoResource


@admin.register(Info)
class InfoAdmin(BaseAdmin, ImportExportModelAdmin):
    """"""
    resource_class = InfoResource

    search_fields = ('name', 'slug')
    list_display = ('name', 'slug')
