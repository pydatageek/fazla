from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget

from places.models import Country
from politics.models import InternationalOrganization
from sources.models import Source
from .models import (
    CountryPopulation, WorldPopulation,
    CountryGdp, WorldGdp,
    Covid19
)


class WorldPopulationResource(resources.ModelResource):
    source = fields.Field(
        attribute='source',
        column_name='source',
        widget=ForeignKeyWidget(Source, field='code')
    )

    class Meta:
        model = WorldPopulation


class CountryPopulationResource(resources.ModelResource):
    source = fields.Field(
        attribute='source',
        column_name='source',
        widget=ForeignKeyWidget(Source, field='code')
    )
    country = fields.Field(
        attribute='country',
        column_name='country',
        widget=ForeignKeyWidget(Country, field='iso2')
    )

    class Meta:
        model = CountryPopulation


class CountryGdpResource(resources.ModelResource):
    """"""
    source = fields.Field(
        attribute='source',
        column_name='source',
        widget=ForeignKeyWidget(Source, field='code')
    )
    country = fields.Field(
        attribute='country',
        column_name='country',
        widget=ForeignKeyWidget(Country, field='iso2')
    )

    class Meta:
        model = CountryGdp


class WorldGdpResource(resources.ModelResource):
    """"""
    source = fields.Field(
        attribute='source',
        column_name='source',
        widget=ForeignKeyWidget(Source, field='code')
    )

    class Meta:
        model = WorldGdp


class Covid19Resource(resources.ModelResource):
    source = fields.Field(
        attribute='source',
        column_name='source',
        widget=ForeignKeyWidget(Source, field='code')
    )
    country = fields.Field(
        attribute='country',
        column_name='country',
        widget=ForeignKeyWidget(Country, field='iso2')
    )

    class Meta:
        model = Covid19
