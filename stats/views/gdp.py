import json

from django.db.models import Q
from django.template import RequestContext
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, ListView, TemplateView

from core.choices import current_year_gdp, titles
from core.utils import LazyEncoder
from places.models import Country
from stats.models import (
    CountryGdp, WorldGdp
)


class CountryGdpDetailView(TemplateView):
    """"""
    slug_field = 'country__slug'
    slug_url_kwarg = 'country_slug'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['stats_type'] = 'gdp'
        context['title'] = Country.objects.filter(
            slug=self.kwargs['country_slug'])[0]
        context['title_page_prefix'] = titles['gdp']
        context['title_page_suffix'] = _('Gross Domestic Product')
        context['year_title'] = titles['year']
        context['growth_rate'] = titles['growth_rate']

        gdp_all = CountryGdp.objects.filter(
            country__slug=self.kwargs['country_slug']).\
            order_by('year').select_related('country')
        gdp = gdp_all.filter(year__lte=current_year_gdp)

        gdp_chart = []
        gdp_pc_chart = []
        gdp_chart_growth = []
        gdp_pc_chart_growth = []
        gdp_chart_ppp = []
        gdp_pc_chart_ppp = []

        for idx, item in enumerate(gdp):
            gdp_chart.append([
                str(item.year), item.gdp_current
            ])
            gdp_pc_chart.append([
                str(item.year), item.gdp_percapita_current
            ])
            gdp_chart_growth.append([
                str(item.year), item.change_rate
            ])
            gdp_pc_chart_growth.append([
                str(item.year), item.change_rate_percapita
            ])
            if item.gdp_ppp_current:
                gdp_chart_ppp.append([
                    str(item.year), item.gdp_ppp_current
                ])
            if item.gdp_percapita_ppp_current:
                gdp_pc_chart_ppp.append([
                    str(item.year), item.gdp_percapita_ppp_current
                ])

        context['gdp_chart'] = json.dumps(
            gdp_chart, cls=LazyEncoder)
        context['gdp_pc_chart'] = json.dumps(
            gdp_pc_chart, cls=LazyEncoder)
        context['gdp_chart_growth'] = json.dumps(
            gdp_chart_growth, cls=LazyEncoder)
        context['gdp_pc_chart_growth'] = json.dumps(
            gdp_pc_chart_growth, cls=LazyEncoder)
        context['gdp_chart_ppp'] = json.dumps(
            gdp_chart_ppp, cls=LazyEncoder)
        context['gdp_pc_chart_ppp'] = json.dumps(
            gdp_pc_chart_ppp, cls=LazyEncoder)

        context['gdp'] = gdp

        return context


class WorldGdpDetailView(TemplateView):
    """"""

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['stats_type'] = 'gdp'
        context['year'] = current_year_gdp
        context['year_title'] = titles['year']
        context['title'] = titles['world']
        context['title_page_prefix'] = titles['gdp']
        context['title_page_suffix'] = _('Gross Domestic Product')

        gdp_all = WorldGdp.objects.all()
        gdp = gdp_all.filter(
            year__lte=current_year_gdp)

        gdp_chart = []
        gdp_pc_chart = []
        gdp_chart_growth = []
        gdp_pc_chart_growth = []
        gdp_chart_ppp = []
        gdp_pc_chart_ppp = []

        for idx, item in enumerate(gdp):
            gdp_chart.append([
                str(item.year), item.gdp_current
            ])
            gdp_pc_chart.append([
                str(item.year), item.gdp_percapita_current
            ])
            gdp_chart_growth.append([
                str(item.year), item.change_rate
            ])
            gdp_pc_chart_growth.append([
                str(item.year), item.change_rate_percapita
            ])
            if item.gdp_ppp_current:
                gdp_chart_ppp.append([
                    str(item.year), item.gdp_ppp_current
                ])
            if item.gdp_percapita_ppp_current:
                gdp_pc_chart_ppp.append([
                    str(item.year), item.gdp_percapita_ppp_current
                ])

        context['gdp_chart'] = json.dumps(
            gdp_chart, cls=LazyEncoder)
        context['gdp_pc_chart'] = json.dumps(
            gdp_pc_chart, cls=LazyEncoder)
        context['gdp_chart_growth'] = json.dumps(
            gdp_chart_growth, cls=LazyEncoder)
        context['gdp_pc_chart_growth'] = json.dumps(
            gdp_pc_chart_growth, cls=LazyEncoder)
        context['gdp_chart_ppp'] = json.dumps(
            gdp_chart_ppp, cls=LazyEncoder)
        context['gdp_pc_chart_ppp'] = json.dumps(
            gdp_pc_chart_ppp, cls=LazyEncoder)

        context['gdp'] = gdp

        context['countries_gdp'] = \
            CountryGdp.objects.\
            exclude(country__slug="andorra").\
            filter(year=current_year_gdp, gdp_current__isnull=False).\
            order_by('-gdp_current').select_related('country')

        return context
