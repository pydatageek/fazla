from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from import_export.admin import ImportExportModelAdmin

from core.admin import BaseAdmin
from .models import Alphabet, Language
from .resources import AlphabetResource, LanguageResource


@admin.register(Alphabet)
class AlphabetAdmin(BaseAdmin, ImportExportModelAdmin):
    """"""
    resource_class = AlphabetResource


@admin.register(Language)
class LanguageAdmin(BaseAdmin, ImportExportModelAdmin):
    """"""
    resource_class = LanguageResource
