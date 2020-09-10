from import_export import resources

from .models import Source


class SourceResource(resources.ModelResource):
    class Meta:
        model = Source
