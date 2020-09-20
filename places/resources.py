from import_export import fields, resources
from import_export.widgets import (
    ForeignKeyWidget, ManyToManyWidget)

from economics.models import Currency
from linguistics.models import Alphabet, Language
from .models import Continent, Country, Region, World


class CountryResource(resources.ModelResource):
    """"""
    parent = fields.Field(
        attribute='parent',
        column_name='parent',
        widget=ForeignKeyWidget(Country, field='iso2'))
    currencies = fields.Field(
        attribute='currencies',
        column_name='currencies',
        widget=ManyToManyWidget(Currency, field='iso3', separator=','))
    languages = fields.Field(
        attribute='languages',
        column_name='languages',
        widget=ManyToManyWidget(Language, field='code', separator=','))
    alphabets = fields.Field(
        attribute='alphabets',
        column_name='alphabets',
        widget=ManyToManyWidget(Alphabet, field='code', separator=','))

    class Meta:
        model = Country


class WorldResource(resources.ModelResource):
    """"""

    class Meta:
        model = World


class ContinentResource(resources.ModelResource):
    """"""

    class Meta:
        model = Continent


class RegionResource(resources.ModelResource):
    """"""

    class Meta:
        model = Region
