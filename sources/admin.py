from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from core.admin import BaseAdmin
from .models import Source
from .resources import SourceResource


@admin.register(Source)
class SourceAdmin(BaseAdmin, ImportExportModelAdmin):
    """"""
    resource_class = SourceResource
