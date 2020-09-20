from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget

from .models import Currency


class CurrencyResource(resources.ModelResource):
    """"""

    class Meta:
        model = Currency
