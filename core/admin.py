from django.contrib import admin
from django.utils.translation import gettext_lazy as _

admin.site.site_header = _('Fazla.NET Admin')
admin.site.site_title = _('Fazla.NET Admin Portal')
admin.site.index_title = _('Welcome to Fazla.NET Admin Portal')


class BaseAdmin(admin.ModelAdmin):
    """Base admin for all models using NameSlugStampedModel model"""
    save_on_top = True

    ordering = ('name',)
    list_display = ('name', 'code', 'unique_code')

    readonly_fields = (
        'added_at', 'added_by', 'updated_at', 'updated_by',
        'slug', 'unique_code')
