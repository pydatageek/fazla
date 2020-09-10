from .base_01 import StampedModel, NameSlugModel, ContentModel


class BaseStampedModel(StampedModel, NameSlugModel):
    """A comprehensive abstract model for items which need
    name, slug fields and also user/time stamps on addition/modification
    """
    class Meta:
        abstract = True


class BaseContentStampedModel(BaseStampedModel, ContentModel):
    """A comprehensive abstract model for items which need
    name, slug, content fields and also user/time stamps on
    addition/modification
    """
    class Meta:
        abstract = True
