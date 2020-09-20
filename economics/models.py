from django.contrib.contenttypes.fields import GenericRelation
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _

from core.models import SeoBaseContentStampedModel, Item


class Currency(SeoBaseContentStampedModel):
    """"""
    iso_numeric = models.PositiveSmallIntegerField(
        _('ISO numeric'))

    iso3 = models.CharField(
        _('ISO3'), max_length=3, unique=True, db_index=True)

    minor_unit = models.PositiveSmallIntegerField(
        _('minor unit'), blank=True, null=True)

    class Meta:
        verbose_name = _('Currency')
        verbose_name_plural = _('Currencies')
