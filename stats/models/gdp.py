from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from core.models import Item, StampedModel
from places.models import Country
from politics.models import InternationalOrganization
from sources.models import Source


class Gdp(StampedModel):
    """"""
    year = models.SmallIntegerField(
        _('year'))

    change = models.IntegerField(
        _('growth'), blank=True, null=True)
    change_rate = models.FloatField(
        _('growth %'), blank=True, null=True)

    change_percapita = models.IntegerField(
        _('growth per capita'), blank=True, null=True)
    change_rate_percapita = models.FloatField(
        _('growth % per capita'), blank=True, null=True)

    gdp_ppp_constant_2017 = models.BigIntegerField(
        _('GDP, PPP (constant 2017 international $)'),
        blank=True, null=True)
    gdp_ppp_current = models.BigIntegerField(
        _('GDP, PPP (current international $)'),
        blank=True, null=True)
    gdp_constant_2010 = models.BigIntegerField(
        _('GDP (constant 2010 US$)'),
        blank=True, null=True)
    gdp_current = models.BigIntegerField(
        _('GDP (current US$)'),
        blank=True, null=True)

    gdp_percapita_ppp_constant_2017 = models.BigIntegerField(
        _('GDP per capita, PPP (constant 2017 international $)'),
        blank=True, null=True)
    gdp_percapita_ppp_current = models.BigIntegerField(
        _('GDP per capita, PPP (current international $)'),
        blank=True, null=True)
    gdp_percapita_constant_2010 = models.BigIntegerField(
        _('GDP per capita (constant 2010 US$)'),
        blank=True, null=True)
    gdp_percapita_current = models.BigIntegerField(
        _('GDP per capita (current US$)'),
        blank=True, null=True)

    # services_rate = models.FloatField(
    #     _('services %'), blank=True, null=True)
    # manufacturing_rate = models.FloatField(
    #     _('manufacturing %'), blank=True, null=True)
    # agriculture_rate = models.FloatField(
    #     _('agriculture %'), blank=True, null=True)

    source = models.ForeignKey(
        Source, on_delete=models.CASCADE,
        related_name='%(class)s', verbose_name=_('source'))

    class Meta:
        abstract = True


class WorldGdp(Gdp):
    """"""

    def __str__(self):
        return f'{self.year}'

    class Meta:
        unique_together = ('year', 'source')
        verbose_name = _('World GDP')
        verbose_name_plural = _('World GDP')

    def get_absolute_url(self):
        return reverse('world-gdp-detail')


class CountryGdp(Gdp):
    """"""
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE,
        related_name='gdps', verbose_name=_('country'))

    def __str__(self):
        return f'{self.country} - {self.year}'

    class Meta:
        unique_together = ('country', 'year', 'source')
        verbose_name = _('Country GDP')
        verbose_name_plural = _('Country GDPs')

    def get_absolute_url(self):
        return reverse(
            'country-gdp-detail', args=[self.country.slug])
