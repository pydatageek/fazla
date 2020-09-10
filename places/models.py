from django.contrib.contenttypes.fields import GenericRelation
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _

from core.models import SeoBaseContentStampedModel, Item


world_land_area = 148940000


class Place(SeoBaseContentStampedModel):
    """"""
    PLACE_TYPES = (
        ('WOR', _('World')),
        ('INT', _('International Region')),
        ('COU', _('Country')),
        ('SC1', _('SubCountry 1')),
        ('SC2', _('SubCountry 2')),
        ('SC3', _('SubCountry 3')),
        ('SC4', _('SubCountry 4')),
    )

    long_name = models.CharField(
        _('long name'), max_length=250, default='', blank=True)

    place_type = models.CharField(
        _('place type'), max_length=3, choices=PLACE_TYPES,
        db_index=True)

    geo_name_id = models.PositiveIntegerField(
        _('geo name id'), default=0, blank=True,
        help_text=_('from geonames.org'))

    latitude = models.FloatField(
        _('latitude'), blank=True, null=True,
        validators=[
            MinValueValidator(-90.0),
            MaxValueValidator(90.0)]
    )
    longitude = models.FloatField(
        _('longitude'), blank=True, null=True,
        validators=[
            MinValueValidator(-180.0),
            MaxValueValidator(180.0)]
    )

    water_area = models.FloatField(
        _('water area'), default=0.0, blank=True,
        help_text=_('km2'))
    land_area = models.FloatField(
        _('land area'), default=0.0, blank=True,
        help_text=_('km2'))
    area = models.FloatField(
        _('total area'), default=0.0, blank=True,
        help_text=_('km2'))

    def land_percent(self):
        if self.land_area + self.water_area:
            return self.land_area / (self.land_area + self.water_area)
        return 0.0
    land_percent.short_description = _('land area %')

    def water_percent(self):
        if self.land_area + self.water_area:
            return self.water_area / (self.land_area + self.water_area)
        return 0.0
    water_percent.short_description = _('water area %')

    def get_water_area(self):
        return intcomma(self.water_area)

    def get_land_area(self):
        return intcomma(self.land_area)

    def get_area(self):
        return intcomma(self.area)

    class Meta:
        abstract = True
        unique_together = ('name', 'place_type')

    def save(self, *args, **kwargs):
        if not self.meta_title:
            self.meta_title = f'{self.name}'

        if not self.area:
            self.area = self.land_area + self.water_area

        super().save(*args, **kwargs)


class World(Place):
    """"""
    item = GenericRelation(Item)

    class Meta:
        verbose_name = _('World')
        verbose_name_plural = _('World')
        ordering = ('id',)

    def get_absolute_url(self):
        return reverse('world-detail')


class Continent(Place):
    """"""
    item = GenericRelation(Item)

    class Meta:
        verbose_name = _('Continent')
        verbose_name_plural = _('Continents')
        ordering = ('id',)

    def get_absolute_url(self):
        return reverse('continent-detail', args=['self.slug'])


class Country(Place):
    """UN defined countries"""
    DRIVINGSIDES = (
        ('R', _('Right')), ('L', _('Left'))
    )

    parent = models.ForeignKey(
        'self', on_delete=models.SET_NULL,
        blank=True, null=True,
        related_name='+', verbose_name=_('parent country'),
        help_text=_('this field is not null for dependent countries'))
    is_independent = models.BooleanField(
        _('is independent'), default=True, editable=False)

    iso_numeric = models.PositiveSmallIntegerField(
        _('ISO numeric'))
    iso2 = models.CharField(
        _('ISO2'), max_length=2, unique=True, db_index=True)
    iso3 = models.CharField(
        _('ISO3'), max_length=3, unique=True, db_index=True)
    iso_3166_2 = models.CharField(
        _('ISO 3166-2'), max_length=25, unique=True)

    e164 = models.CharField(
        _('E164'), max_length=25, default='', blank=True)
    phone_code = models.CharField(
        _('phone code'), max_length=25)
    fips = models.CharField(
        _('FIPS'), max_length=25, default='', blank=True)
    tld = models.CharField(
        _('TLD'), max_length=5, default='', blank=True,
        help_text=_('Top Level Domain'))

    driving_side = models.CharField(
        _('driving side'), max_length=1,
        default='R', choices=DRIVINGSIDES)

    item = GenericRelation(Item)

    class Meta:
        verbose_name = _('Country')
        verbose_name_plural = _('Countries')
        ordering = ('id',)

    def get_absolute_url(self):
        return reverse('country-detail', args=['self.slug'])

    def save(self, *args, **kwargs):
        self.is_independent = False if self.parent else True
        super().save(*args, **kwargs)

    @cached_property
    def area_rate(self):
        return (self.area / world_land_area) * 100
