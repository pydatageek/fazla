from django.contrib.contenttypes.fields import GenericRelation
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import Case, F, Q, Sum, When
from django.urls import reverse
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _

from core.models import Item, StampedModel
from places.models import Country
from politics.models import InternationalOrganization
from sources.models import Source


class Covid19Manager(models.Manager):
    """"""

    # @cached_property
    def world(self):
        """"""
        return self.values('date').annotate(
            world_total_confirmed=Sum('total_confirmed'),
            world_new_confirmed=Sum('new_confirmed'),
            world_total_death=Sum('total_death'),
            world_new_death=Sum('new_death')
        ).annotate(
            world_death_rate=Case(
                When(world_total_confirmed=0, then=None),
                default=100.0*F('world_total_death') /
                F('world_total_confirmed'),
                output_field=models.FloatField())
        ).order_by('date')


class Covid19(StampedModel):
    """
    source: https://covid19.who.int/info
    """

    country = models.ForeignKey(
        Country, on_delete=models.CASCADE,
        related_name='covid19s', verbose_name=_('country'))
    date = models.DateField(
        _('date'))

    new_confirmed = models.IntegerField(
        _('new confirmed'), default=0, blank=True)
    total_confirmed = models.IntegerField(
        _('total confirmed'), default=0, blank=True)
    new_death = models.IntegerField(
        _('new death'), default=0, blank=True)
    total_death = models.IntegerField(
        _('total death'), default=0, blank=True)
    # recovered = models.IntegerField(
    #     _('recovered'), default=0, blank=True)
    # active = models.IntegerField(
    #     _('active'), default=0, blank=True)

    source = models.ForeignKey(
        Source, on_delete=models.CASCADE,
        related_name='%(class)s', verbose_name=_('source'))

    @cached_property
    def death_rate(self):
        if self.total_confirmed != 0:
            return 100.0 * self.total_death / self.total_confirmed
        return 0.0

    objects = Covid19Manager()

    class Meta:
        unique_together = ('country', 'date')
        verbose_name = _('Covid19')
        verbose_name_plural = _('Covid19')

    def get_absolute_url(self):
        return reverse(
            'country-covid19-detail', args=[self.country.slug])
