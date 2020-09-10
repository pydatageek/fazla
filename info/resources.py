from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget

from .models import Info


class InfoResource(resources.ModelResource):
    """"""

    class Meta:
        model = Info
