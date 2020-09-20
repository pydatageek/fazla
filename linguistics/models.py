from django.contrib.contenttypes.fields import GenericRelation
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _

from core.models import SeoBaseContentStampedModel, Item


class Alphabet(SeoBaseContentStampedModel):
    """"""

    class Meta:
        verbose_name = _('Alphabet')
        verbose_name_plural = _('Alphabets')


class Language(SeoBaseContentStampedModel):
    """"""
    family_text = models.CharField(
        _('family'), max_length=250, default='', blank=True)

    native_name = models.CharField(
        _('native name'), max_length=250, default='', blank=True)

    code = models.CharField(
        _('code'), max_length=3, unique=True, db_index=True)

    iso2 = models.CharField(
        _('ISO2'), max_length=2, blank=True, null=True)
    iso3 = models.CharField(
        _('ISO3'), max_length=3, blank=True, null=True)
    _639_2_b = models.CharField(
        _('639-2/B'), max_length=5, blank=True, null=True)
    _639_3 = models.CharField(
        _('639-3'), max_length=100, blank=True, null=True)

    notes = models.TextField(
        _('notes'), default='', blank=True)

    class Meta:
        verbose_name = _('Language')
        verbose_name_plural = _('Languages')
