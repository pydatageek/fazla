from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from core.models import Item
from places.models import Country
from politics.models import InternationalOrganization
from sources.models import Source


class Population(models.Model):
    """"""
    GENDERS = (
        ('F', 'Female'), ('M', 'Male'), ('T', 'Total')
    )
    year = models.SmallIntegerField(
        _('year'))

    change_ratio = models.FloatField(
        _('change'), blank=True, null=True)
    gender = models.CharField(
        _('gender'), max_length=1, choices=GENDERS, default='F')
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
    population = models.BigIntegerField(
        _('population'))

    item = GenericRelation(Item)

    def __str__(self):
        return f'{self.year} - {self.get_gender_display()}'

    class Meta:
        unique_together = ('year', 'gender', 'source')
        verbose_name = _('World Population')
        verbose_name_plural = _('World Populations')


class InternationalOrganizationPopulation(Population):
    """"""
    population = models.BigIntegerField(
        _('population'))

    organization = models.ForeignKey(
        InternationalOrganization, on_delete=models.CASCADE,
        related_name='populations', verbose_name=_('organization'))

    item = GenericRelation(Item)

    def __str__(self):
        return f'{self.organization} - {self.year} - {self.get_gender_display()}'

    class Meta:
        unique_together = ('organization', 'year', 'gender', 'source')
        verbose_name = _('International Organization Population')
        verbose_name_plural = _('International Organization Populations')


class CountryPopulation(Population):
    """"""
    population = models.IntegerField(
        _('population'))

    country = models.ForeignKey(
        Country, on_delete=models.CASCADE,
        related_name='populations', verbose_name=_('country'))

    item = GenericRelation(Item)

    def __str__(self):
        return f'{self.country} - {self.year} - {self.get_gender_display()}'

    class Meta:
        # unique_together = ('country', 'year', 'gender', 'source')
        verbose_name = _('Country Population')
        verbose_name_plural = _('Country Populations')

    # def get_absolute_url(self, *args, **kwargs):
    #     # return reverse('country-population-detail', kwargs={
    #     #     'country_slug': 'self.country.slug'})
    #     return reverse(
    #         'country-population-detail',
    #         args=['country_slug'])

    # def total_population(self):
    #     return self.population
