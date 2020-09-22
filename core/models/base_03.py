from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .base_01 import ContentModel, SeoModel
from .base_02 import BaseStampedModel, BaseContentStampedModel


class SeoBaseStampedModel(BaseStampedModel, SeoModel):
    """"""
    publish_at = models.DateTimeField(
        _('publish date'), blank=True, null=True)
    unpublish_at = models.DateTimeField(
        _('unpublish date'), blank=True, null=True)
    is_published = models.BooleanField(
        _('is published'), default=False, editable=False)

    @property
    def meta_author(self):
        return self.added_by

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.meta_title:
            self.meta_title = f'{self.name}'

        if not self.added_at:
            self.added_at = timezone.now()
        if not self.publish_at:
            self.publish_at = self.added_at

        self.is_published = \
            True if timezone.now() - self.publish_at else False

        if self.unpublish_at:
            if (timezone.now() - self.publish_at) \
                    and (self.unpublish_at - timezone.now()):
                self.is_published = True
            else:
                self.is_published = False

        super().save(*args, **kwargs)


class SeoBaseContentStampedModel(SeoBaseStampedModel, ContentModel):
    """"""
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):

        if not self.meta_description:
            self.meta_description = f'{self.short_content}'

        super().save(*args, **kwargs)


class Item(models.Model):
    """"""
    # unique_code = models.CharField(
    #     _('unique code'), max_length=9, default='', blank=True,
    #     unique=True, db_index=True)

    content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey(
        'content_type', 'object_id')

    # def __str__(self):
    #     return self.unique_code

    class Meta:
        verbose_name = _('Item')
        verbose_name_plural = _('Items')

    # def save(self, *args, **kwargs):
    #     class_short_name = self.__class__.__name__.lower()[:6:2]
    #     class_short_name = class_short_name.strip()
    #     len_csn = len(class_short_name)

    #     if not self.unique_code:
    #         self.unique_code = class_short_name + random_chars(9-len_csn)

    #     super().save(*args, **kwargs)
