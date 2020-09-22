from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from core.models import Item, StampedModel
from places.models import Country
from politics.models import InternationalOrganization
from sources.models import Source


class Population(StampedModel):
    """"""
    year = models.SmallIntegerField(
        _('year'))

    change = models.IntegerField(
        _('change'), blank=True, null=True)
    change_rate = models.FloatField(
        _('change %'), blank=True, null=True)
    fertility_rate = models.FloatField(
        _('fertility'), blank=True, null=True)
    median_age = models.FloatField(
        _('median age'), blank=True, null=True)
    density = models.FloatField(
        _('density'), blank=True, null=True)

    source = models.ForeignKey(
        Source, on_delete=models.CASCADE,
        related_name='%(class)s', verbose_name=_('source'))

    class Meta:
        abstract = True


class WorldPopulation(Population):
    """"""
    # country = models.ForeignKey(
    #     Country, on_delete=models.CASCADE,
    #     related_name='populations', verbose_name=_('country'))
    female = models.BigIntegerField(
        _('female'), blank=True, null=True)
    male = models.BigIntegerField(
        _('male'), blank=True, null=True)
    total = models.BigIntegerField(
        _('total'), blank=True, null=True)

    item = GenericRelation(Item)

    def male_percent(self):
        if self.total and self.male and self.female:
            return self.male * 100 / self.total
    male_percent.short_description = _('male %')

    def female_percent(self):
        if self.total and self.male and self.female:
            return self.female * 100 / self.total
    female_percent.short_description = _('female %')

    def __str__(self):
        return f'{self.year}'

    class Meta:
        unique_together = ('year', 'source')
        verbose_name = _('World Population')
        verbose_name_plural = _('World Population')

    def get_absolute_url(self):
        return reverse('world-population-detail')


class InternationalOrganizationPopulation(Population):
    """"""
    female = models.BigIntegerField(
        _('female'), blank=True, null=True)
    male = models.BigIntegerField(
        _('male'), blank=True, null=True)
    total = models.BigIntegerField(
        _('total'), blank=True, null=True)

    organization = models.ForeignKey(
        InternationalOrganization, on_delete=models.CASCADE,
        related_name='populations', verbose_name=_('organization'))

    item = GenericRelation(Item)

    def male_percent(self):
        if self.total and self.male and self.female:
            return self.male * 100 / self.total
    male_percent.short_description = _('male %')

    def female_percent(self):
        if self.total and self.male and self.female:
            return self.female * 100 / self.total
    female_percent.short_description = _('female %')

    def __str__(self):
        return f'{self.organization} - {self.year}'

    class Meta:
        unique_together = ('organization', 'year', 'source')
        verbose_name = _('International Organization Population')
        verbose_name_plural = _('International Organization Populations')


class CountryPopulation(Population):
    """"""
    female = models.IntegerField(
        _('female'), blank=True, null=True)
    male = models.IntegerField(
        _('male'), blank=True, null=True)
    total = models.IntegerField(
        _('total'), blank=True, null=True)

    country = models.ForeignKey(
        Country, on_delete=models.CASCADE,
        related_name='populations', verbose_name=_('country'))

    item = GenericRelation(Item)

    def male_percent(self):
        if self.total and self.male and self.female:
            return self.male * 100 / self.total
    male_percent.short_description = _('male %')

    def female_percent(self):
        if self.total and self.male and self.female:
            return self.female * 100 / self.total
    female_percent.short_description = _('female %')

    def __str__(self):
        return f'{self.country} - {self.year}'

    class Meta:
        unique_together = ('country', 'year', 'source')
        verbose_name = _('Country Population')
        verbose_name_plural = _('Country Populations')

    def get_absolute_url(self):
        return reverse(
            'country-population-detail', args=[self.country.slug])

    # def get_absolute_url(self, *args, **kwargs):
    #     # return reverse('country-population-detail', kwargs={
    #     #     'country_slug': 'self.country.slug'})
    #     return reverse(
    #         'country-population-detail',
    #         args=['country_slug'])

    # def total_population(self):
    #     return self.population
