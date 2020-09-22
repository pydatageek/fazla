from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import SeoBaseContentStampedModel, Item


class Source(SeoBaseContentStampedModel):
    """"""
    parent_text = models.CharField(
        max_length=100, default='', blank=True)
    url = models.URLField(
        _('url'), default='', blank=True)

    item = GenericRelation(Item)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Source')
        verbose_name_plural = _('Sources')

# class Unit(NameSlugModel, ContentModel):
#     """"""

#     def __str__(self):
#         return self.name
