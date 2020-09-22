from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from .models import (
    CountryPopulation, WorldPopulation,
    CountryGdp, WorldGdp
)
from .resources import (
    CountryPopulationResource, WorldPopulationResource,
    CountryGdpResource, WorldGdpResource
)


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


@admin.register(CountryGdp)
class CountryGdpAdmin(ImportExportModelAdmin):
    """"""
    resource_class = CountryGdpResource

    search_fields = ('country__name', 'year')
    list_display = (
        'country', 'year',
        'gdp_current', 'gdp_percapita_current')


@admin.register(WorldGdp)
class WorldGdpAdmin(ImportExportModelAdmin):
    """"""
    resource_class = WorldGdpResource

    search_fields = ('year',)
    list_display = (
        'year',
        'gdp_current', 'gdp_percapita_current')
