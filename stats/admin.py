from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from .models import (
    CountryPopulation, WorldPopulation,
    InternationalOrganizationPopulation)
from .resources import (
    CountryPopulationResource, WorldPopulationResource,
    InternationalOrganizationPopulationResource)


@admin.register(CountryPopulation)
class CountryPopulationAdmin(ImportExportModelAdmin):
    """"""
    resource_class = CountryPopulationResource

    search_fields = ('country__name', 'year')
    list_display = ('country', 'year', 'total', 'density')


@admin.register(WorldPopulation)
class WorldPopulationAdmin(ImportExportModelAdmin):
    """"""
    resource_class = WorldPopulationResource

    search_fields = ('year',)
    list_display = ('year', 'total', 'change_rate', 'median_age',
                    'density', 'fertility_rate')


@admin.register(InternationalOrganizationPopulation)
class InternationalOrganizationPopulationAdmin(ImportExportModelAdmin):
    """"""
    resource_class = InternationalOrganizationPopulationResource

    search_fields = ('organization__name', 'year')
    list_display = ('organization', 'year', 'total', 'change_rate',
                    'median_age', 'density', 'fertility_rate')
