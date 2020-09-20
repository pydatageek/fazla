from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from core.models import Item
from places.models import Country
from politics.models import InternationalOrganization
from sources.models import Source


class Gdp(models.Model):
    """"""
    year = models.SmallIntegerField(
        _('year'))

    change = models.IntegerField(
        _('change'), blank=True, null=True)
    change_rate = models.FloatField(
        _('change %'), blank=True, null=True)

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

    gdp_percapita__ppp_constant_2017 = models.BigIntegerField(
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

    services_rate = models.FloatField(
        _('services %'), blank=True, null=True)
    manufacturing_rate = models.FloatField(
        _('manufacturing %'), blank=True, null=True)
    agriculture_rate = models.FloatField(
        _('agriculture %'), blank=True, null=True)

    source = models.ForeignKey(
        Source, on_delete=models.CASCADE,
        related_name='%(class)s', verbose_name=_('source'))

    class Meta:
        abstract = True
