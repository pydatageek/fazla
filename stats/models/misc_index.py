from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.db.models import Count, Q
from django.urls import reverse
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _

from core.models import Item, StampedModel
from places.models import Country
from sources.models import Source


class Hdi(StampedModel):
    """"""
    year = models.SmallIntegerField(
        _('year'))

    hdi_value = models.FloatField(
        _('hdi'))

    source = models.ForeignKey(
        Source, on_delete=models.CASCADE,
        related_name='%(class)s', verbose_name=_('source'))

    class Meta:
        abstract = True


class WorldHdi(Hdi):
    """"""

    def __str__(self):
        return f'{self.year}'

    class Meta:
        unique_together = ('year', 'source')
        verbose_name = _('World HDI')
        verbose_name_plural = _('World HDI')

    def get_absolute_url(self):
        return reverse('world-hdi-detail')


class CountryHdi(Hdi):
    """"""
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE,
        related_name='hdis', verbose_name=_('country'))

    # @cached_property
    # def ranking(self):
    #     aggregate = CountryHdi.objects.\
    #         filter(Q(hdi_value__gt=self.hdi_value) & Q(year=self.year)).\
    #         aggregate(ranking=Count('hdi_value'))
    #     return aggregate['ranking'] + 1

    def __str__(self):
        return f'{self.country} - {self.year}'

    class Meta:
        unique_together = ('country', 'year', 'source')
        verbose_name = _('Country HDI')
        verbose_name_plural = _('Country HDIs')

    def get_absolute_url(self):
        return reverse(
            'country-hdi-detail', args=[self.country.slug])
