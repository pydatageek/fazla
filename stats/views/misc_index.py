import json

from django.db.models import F, Q, Window, Value, Subquery
from django.db.models.functions import Rank, DenseRank, Lag
from django.template import RequestContext
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, ListView, TemplateView

from core.choices import titles
from core.utils import LazyEncoder
from places.models import Country
from stats.models import (
    CountryHdi, WorldHdi
)


class CountryHdiDetailView(TemplateView):
    """"""
    slug_field = 'country__slug'
    slug_url_kwarg = 'country_slug'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['stats_type'] = 'hdi'
        context['title'] = Country.objects.filter(
            slug=self.kwargs['country_slug'])[0]
        context['title_page_prefix'] = titles['hdi']
        context['title_page_suffix'] = _('Human Development Index')
        context['year_title'] = titles['year']

        ranking = Window(
            expression=DenseRank(),
            partition_by=F("year"),
            order_by=F("hdi_value").desc()
        )

        # hdi = CountryHdi.objects.annotate(ranking=ranking).filter(
        #     country__slug=self.kwargs['country_slug']).\
        #     order_by('year').select_related('country')

        # hdi2 = CountryHdi.objects.annotate(ranking=ranking)
        hdi = CountryHdi.objects.filter(
            country__slug=self.kwargs['country_slug']).\
            order_by('-year').select_related(
                'country')

        # latest_year = CountryHdi.objects.latest('year').year

        context['hdi'] = hdi

        return context


class WorldHdiDetailView(TemplateView):
    """"""

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['stats_type'] = 'hdi'
        context['year_title'] = titles['year']
        context['title'] = titles['world']
        context['title_page_prefix'] = titles['hdi']
        context['title_page_suffix'] = _('Human Development Index')

        hdi = WorldHdi.objects.all()
        latest_year = WorldHdi.objects.latest('year').year

        dense_rank_by_year = Window(
            expression=DenseRank(),
            partition_by=F('year'),
            order_by=F('hdi_value').desc()
        )

        countries_hdi = CountryHdi.objects.\
            filter(year=latest_year).\
            annotate(ranking=dense_rank_by_year).\
            order_by('-hdi_value').select_related('country')

        context['hdi'] = hdi
        context['latest_year'] = latest_year
        context['countries_hdi'] = countries_hdi

        return context
