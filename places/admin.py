from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from import_export.admin import ImportExportModelAdmin

from core.admin import BaseAdmin
from .models import Continent, Country, World
from .resources import (
    ContinentResource, CountryResource, WorldResource)


@admin.register(Country)
class CountryAdmin(BaseAdmin, ImportExportModelAdmin):
    """"""
    resource_class = CountryResource

    search_fields = (
        'name', 'iso_numeric', 'iso_3166_2')
    list_display = (
        'name', 'is_independent', 'iso2', 'iso_numeric',
        'slug', 'unique_code', 'area'
    )

    readonly_fields = (
        'added_at', 'added_by', 'updated_at', 'updated_by',
        'is_published', 'meta_author',
        'unique_code',
        'url_slug_code', 'url_slug_chars', 'url_slug_id',
        'land_percent', 'water_percent',
        'is_independent'
    )
    fieldsets = (
        (_('Base info'), {
            'fields': (
                ('name', 'long_name'), ('code', 'slug', 'unique_code'),
                'short_content', 'content',
                'url_slug_chars', 'url_slug_code', 'url_slug_id',
            ),
        }),
        (_('SEO info'), {
            'fields': (
                'meta_title', 'meta_description',
                'meta_author',  # 'meta_keywords',
                ('publish_at', 'is_published'), 'unpublish_at',
            ),
        }),
        (_('Place info'), {
            'fields': (
                'place_type', 'geo_name_id',
                ('latitude', 'longitude'),
                ('water_area', 'land_percent'),
                ('land_area', 'water_percent'), 'area',
            ),
        }),
        (_('Country info'), {
            'fields': (
                ('parent', 'is_independent'), ('iso_numeric', 'iso2'),
                ('iso3', 'iso_3166_2'),
                ('e164', 'phone_code'), 'fips', 'tld', 'driving_side',
            ),
        }),
        (_('Meta info'), {
            'fields': (
                ('added_at', 'added_by'), ('updated_at', 'updated_by'),
            ),
        }),
    )


@admin.register(World)
class WorldAdmin(BaseAdmin, ImportExportModelAdmin):
    """"""
    resource_class = WorldResource


@admin.register(Continent)
class ContinentAdmin(BaseAdmin, ImportExportModelAdmin):
    """"""
    resource_class = ContinentResource
