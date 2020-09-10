from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget

from .models import Continent, Country, World


class CountryResource(resources.ModelResource):
    """"""
    parent = fields.Field(
        attribute='parent',
        column_name='parent',
        widget=ForeignKeyWidget(Country, field='iso2'))

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
