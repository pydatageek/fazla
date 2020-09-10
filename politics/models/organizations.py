from django.contrib.contenttypes.fields import GenericRelation
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from core.models import SeoBaseContentStampedModel, Item


class Organization(SeoBaseContentStampedModel):
    """"""
    ORGANIZATION_TYPES = (
        ('UIGO', 'Umbrella Intergovernmental organization'),
        ('IGO', 'Intergovernmental organization'),
        ('INGO', 'International non-governmental organization'),
        ('OR', 'Organ'),
        ('CO', 'Convention'),
        ('PR', 'Programme'),
        ('SA', 'Statistical Area'),
    )
    organization_type = models.CharField(
        _('type'), max_length=4, default='OR', choices=ORGANIZATION_TYPES)
    is_active = models.BooleanField(
        _('is active'), default=True)
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, blank=True, null=True,
        related_name='+', verbose_name='parent')
    headquarters = models.CharField(
        _('headquarters'), max_length=100, default='', blank=True)
    established_at = models.DateField(
        _('established at'), blank=True, null=True)
    url = models.URLField(
        _('url'), default='', blank=True)

    # logo =

    class Meta:
        abstract = True
        # verbose_name = _('Organization')
        # verbose_name_plural = _('Organizations')

    def save(self, *args, **kwargs):
        if not self.meta_title:
            self.meta_title = f'{self.name}'

        super().save(*args, **kwargs)


class InternationalOrganization(Organization):
    """"""
    iso_numeric = models.PositiveSmallIntegerField(
        _('ISO numeric'), blank=True, null=True)

    item = GenericRelation(Item)

    class Meta:
        verbose_name = _('International Organization')
        verbose_name_plural = _('International Organizations')


class LocalOrganization(Organization):
    """"""
    item = GenericRelation(Item)

    class Meta:
        verbose_name = _('Local Organization')
        verbose_name_plural = _('Local Organizations')
