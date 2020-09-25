from datetime import datetime, timedelta
import json
import requests
import time

from django.contrib.auth.decorators import user_passes_test
from django.db.models import Q, Sum, Max
from django.shortcuts import render
from django.template import RequestContext
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, ListView, TemplateView

from core.choices import titles
from core.utils import LazyEncoder
from places.models import Country
from stats.models import Covid19


def check_admin(user):
    return user.is_superuser


class CountryCovid19DetailView(TemplateView):
    """"""
    slug_field = 'country__slug'
    slug_url_kwarg = 'country_slug'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['stats_type'] = 'covid19'
        context['title'] = Country.objects.filter(
            slug=self.kwargs['country_slug'])[0]
        context['title_page_prefix'] = _('Covid 19')

        covid = Covid19.objects.filter(
            country__slug=self.kwargs['country_slug']).\
            order_by('date').select_related('country')
        latest_date = Covid19.objects.latest('date').date

        covid_chart = []

        for idx, item in enumerate(covid):
            covid_chart.append([
                str(item.date), item.total_confirmed
            ])

        context['covid_chart'] = json.dumps(
            covid_chart, cls=LazyEncoder)

        context['title_page_suffix'] = _('Statistics') + f' ({latest_date})'
        context['latest_date'] = latest_date
        context['covid'] = covid

        return context


class WorldCovid19DetailView(TemplateView):
    """"""

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['stats_type'] = 'covid19'
        context['title'] = titles['world']
        context['title_page_prefix'] = _('Covid 19')

        covid_world = Covid19.objects.world()
        latest_date = Covid19.objects.latest('date').date

        context['title_page_suffix'] = _('Statistics') + f' ({latest_date})'
        context['latest_date'] = latest_date
        context['covid'] = covid_world

        context['countries_covid'] = Covid19.objects.filter(
            date=latest_date).select_related('country')

        return context
