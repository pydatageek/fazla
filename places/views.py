import json

from django.db.models import Q, Prefetch
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import get_object_or_404, render
from django.template import RequestContext
from django.urls import resolve
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.views.defaults import server_error
from django.views.generic import DetailView, ListView, TemplateView

from core.choices import titles, current_year, current_year_gdp
from economics.models import Currency
from linguistics.models import Alphabet, Language
from stats.models import (
    CountryPopulation, WorldPopulation, CountryGdp, WorldGdp,
    Covid19)
from .models import Continent, Country, World


class CountryListView(ListView):
    """"""

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(is_alive=True)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = _('Countries')
        return context


class CountryDetailView(DetailView):
    """"""
    model = Country

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(is_alive=True).prefetch_related(
            Prefetch(
                'currencies',
                Currency.objects.only('name')),
            Prefetch(
                'languages',
                Language.objects.only('name')),
            Prefetch(
                'alphabets',
                Alphabet.objects.only('name')),
        )

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = self.object.name
        context['title_page_prefix'] = _('Country')
        context['population'] = CountryPopulation.objects.filter(
            country__slug=self.kwargs['slug'], year=current_year).first()
        # context['gdp'] = CountryGdp.objects.filter(
        #     country__slug=self.kwargs['slug'], year=current_year_gdp).first()
        context['gdp'] = CountryGdp.objects.filter(
            country__slug=self.kwargs['slug']).order_by('-year').first()

        context['covid19'] = Covid19.objects.filter(
            country__slug=self.kwargs['slug']).order_by('-date').first()

        return context


class WorldDetailView(TemplateView):
    """"""

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = _('World')
        context['world'] = World.objects.all().first()
        context['population'] = WorldPopulation.objects.filter(
            year=current_year).first()
        context['gdp'] = WorldGdp.objects.filter(year=current_year_gdp).first()

        # latest_date = Covid19.objects.latest('date').date
        context['covid19'] = Covid19.objects.world().order_by('-date').first()
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
