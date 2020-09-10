from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget

from places.models import Country
from politics.models import InternationalOrganization
from sources.models import Source
from .models import (
    CountryPopulation, WorldPopulation,
    InternationalOrganizationPopulation)


class WorldPopulationResource(resources.ModelResource):
    source = fields.Field(
        attribute='source',
        column_name='source',
        widget=ForeignKeyWidget(Source, field='code')
    )

    class Meta:
        model = WorldPopulation


class InternationalOrganizationPopulationResource(resources.ModelResource):
    source = fields.Field(
        attribute='source',
        column_name='source',
        widget=ForeignKeyWidget(Source, field='code')
    )
    organization = fields.Field(
        attribute='organization',
        column_name='code',
        widget=ForeignKeyWidget(InternationalOrganization, field='code')
    )

    class Meta:
        model = InternationalOrganizationPopulation


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
