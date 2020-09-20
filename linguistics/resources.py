from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget

from .models import Alphabet, Language


class AlphabetResource(resources.ModelResource):
    """"""

    class Meta:
        model = Alphabet


class LanguageResource(resources.ModelResource):
    """"""

    class Meta:
        model = Language
