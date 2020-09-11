from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.shortcuts import get_object_or_404
from django.urls import resolve
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.utils.translation import gettext_lazy as _
from django.views.decorators.cache import cache_page
from django.views.generic import DetailView, ListView, TemplateView

from info.models import Info
from places.models import Continent, Country, World
from politics.models import InternationalOrganization
from stats.models import (
    CountryPopulation, InternationalOrganizationPopulation,
    WorldPopulation
)

year = timezone.now().year
CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


class HomeView(TemplateView):
    """"""


class CountryListView(ListView):
    """"""
    model = Country

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = _('Countries')
        return context


@method_decorator(cache_page(CACHE_TTL), name='dispatch')
class CountryDetailView(DetailView):
    """"""
    model = Country

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = self.object.name
        context['title_page_prefix'] = _('Country')
        context['population'] = CountryPopulation.objects.filter(
            country__slug=self.kwargs['slug'], year=2020).first()
        return context


@method_decorator(cache_page(CACHE_TTL), name='dispatch')
class WorldDetailView(TemplateView):
    """"""

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = _('World')
        context['world'] = World.objects.all().first()
        context['population'] = WorldPopulation.objects.filter(
            year=2020).first()
        return context


class ContinentListView(ListView):
    """"""
    model = Continent

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = _('Continents')
        return context


class ContinentDetailView(DetailView):
    """"""
    model = Continent

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = self.object.name
        context['title_page_prefix'] = _('Continent')
        return context


@method_decorator(cache_page(CACHE_TTL), name='dispatch')
class CountryPopulationDetailView(ListView):
    """"""
    model = CountryPopulation
    slug_field = 'country__slug'
    slug_url_kwarg = 'country_slug'

    def get_queryset(self):
        qs = super().get_queryset()
        # country_slug = self.kwargs['country_slug']
        return qs.filter(
            country__slug=self.kwargs['country_slug']).order_by('year')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # context['title'] = self.object.country.name
        context['title'] = Country.objects.filter(
            slug=self.kwargs['country_slug'])[0]
        context['title_page_prefix'] = _('Population')
        context['growth_rate'] = _('Growth Rate')
        context['median_age'] = _('Median Age')
        context['density'] = _('Population Density')
        context['fertility'] = _('Fertility Rate')
        return context


class InternationalOrganizationPopulationDetailView(ListView):
    """"""
    model = InternationalOrganizationPopulation
    slug_field = 'organization__slug'
    slug_url_kwarg = 'organization_slug'

    def get_queryset(self):
        qs = super().get_queryset()
        # country_slug = self.kwargs['country_slug']
        return qs.filter(
            organization__slug=self.kwargs['organization_slug'])

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # context['title'] = self.object.country.name
        context['title'] = InternationalOrganization.objects.filter(
            slug=self.kwargs['organization_slug'])[0]
        context['title_page_prefix'] = _('Population')
        return context


@method_decorator(cache_page(CACHE_TTL), name='dispatch')
class WorldPopulationDetailView(ListView):
    """"""
    model = WorldPopulation

    def get_queryset(self):
        qs = super().get_queryset()
        # country_slug = self.kwargs['country_slug']
        return qs.all().order_by('year')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = _('World')
        context['title_page_prefix'] = _('Population')
        context['growth_rate'] = _('Growth Rate')
        context['median_age'] = _('Median Age')
        context['density'] = _('Population Density')
        context['fertility'] = _('Fertility Rate')
        context['countries_population'] = \
            CountryPopulation.objects.filter(
                year=year, total__isnull=False).order_by('total').select_related('country')
        return context


@method_decorator(cache_page(CACHE_TTL), name='dispatch')
class InfoTemplateView(TemplateView):
    """"""

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        current_url = resolve(self.request.path_info).url_name

        slug = ''
        title = ''

        if (current_url == 'phone-code-list'):
            slug = 'international-phone-codes'
            title = _('International Phone Codes')
        elif current_url == 'country-code-list':
            slug = 'country-codes-iso-un-fips'
            title = _('Country Codes (ISO, UN, FIPS)')
        elif current_url == 'driving-side-list':
            slug = 'country-driving-sides'
            title = _('Countries Driving Sides')
        elif current_url == 'country-area-list':
            slug = 'country-surface-areas'
            title = _('Country Surface Areas')
        elif current_url == 'country-tld-list':
            slug = 'international-top-level-domains-tlds'
            title = _('International Top Level Domains (TLDs)')
        else:
            slug = ''

        # area_per_capita_list = []
        # area_per_capita = -1
        # population_list = CountryPopulation.objects.filter(
        #     year=year)
        country_list = Country.objects.exclude(iso2='00')
        # for pop in population_list:
        #     for country in country_list:
        #         if pop.country == country:
        #             area_per_capita = country.area / pop.total

        context['object'] = Info.objects.filter(slug=slug).first()
        context['object_list'] = country_list
        context['title'] = title
        context['title_page_prefix'] = _('Info')
        return context


class InfoDetailView(DetailView):
    """"""
    model = Info

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        current_url = resolve(self.request.path_info).url_name

        context['title'] = self.object.name
        context['title_page_prefix'] = _('Info')
        return context


class InfoListView(ListView):
    """"""
    model = Info

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = _('Info')
        return context
