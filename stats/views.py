import json

from django.db.models import Q
from django.template import RequestContext
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, ListView, TemplateView

from core.choices import titles
from core.utils import LazyEncoder
from places.models import Country
from .models import (
    CountryPopulation, InternationalOrganizationPopulation,
    WorldPopulation
)
from .services import get_population

current_year = timezone.now().year
years_future = [y for y in range(current_year+1, 2101) if y % 5 == 0]


class CountryPopulationDetailView(TemplateView):
    """"""
    slug_field = 'country__slug'
    slug_url_kwarg = 'country_slug'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = Country.objects.filter(
            slug=self.kwargs['country_slug'])[0]
        context['title_page_prefix'] = titles['pop']
        context['year_title'] = titles['year']
        context['growth_rate'] = titles['growth_rate']
        context['median_age'] = titles['median_age']
        context['density'] = titles['density']
        context['fertility'] = titles['fertility_rate']

        population = CountryPopulation.objects.filter(
            country__slug=self.kwargs['country_slug']).\
            order_by('year').select_related('country')

        wp = population.filter(year__lte=current_year)

        wp_future = population.filter(year__in=years_future)

        wp_chart = [
            # [
            #     titles['year'], titles['total'],
            #     titles['female'], titles['male'],
            # ]
        ]

        wp_chart_growth = [
            [
                titles['year'], titles['growth_rate'],
            ]
        ]
        wp_chart_density = [
            [
                titles['year'], titles['density'],
            ]
        ]
        wp_chart_fertility = [
            # [
            #     titles['year'], titles['fertility_rate'],
            # ]
        ]
        wp_chart_median_age = [
            # [
            #     titles['year'], titles['median_age'],
            # ]
        ]

        wp_future_chart = [
            # [
            #     titles['year'], titles['total'],
            #     titles['female'], titles['male'],
            # ]
        ]

        wp_future_chart_growth = [
            [
                titles['year'], titles['growth_rate'],
            ]
        ]
        wp_future_chart_density = [
            [
                titles['year'], titles['density'],
            ]
        ]
        wp_future_chart_fertility = [
            # [
            #     titles['year'], titles['fertility_rate'],
            # ]
        ]
        wp_future_chart_median_age = [
            # [
            #     titles['year'], titles['median_age'],
            # ]
        ]

        for idx, item in enumerate(wp):
            wp_chart.append([
                str(item.year), item.total,
                item.female, item.male
            ])
            wp_chart_growth.append([
                str(item.year), item.change_rate,
            ])
            wp_chart_density.append([
                str(item.year), item.density,
            ])
            if (idx+1) % 5 == 0:
                if item.fertility_rate:
                    wp_chart_fertility.append([
                        str(item.year), item.fertility_rate,
                    ])
                if item.median_age:
                    wp_chart_median_age.append([
                        str(item.year), item.median_age,
                    ])

        for item in wp_future:
            wp_future_chart.append([
                str(item.year), item.total,
                item.female, item.male
            ])
            wp_future_chart_growth.append([
                str(item.year), item.change_rate,
            ])
            wp_future_chart_density.append([
                str(item.year), item.density,
            ])
            if item.fertility_rate:
                wp_future_chart_fertility.append([
                    str(item.year), item.fertility_rate,
                ])
            if item.median_age:
                wp_future_chart_median_age.append([
                    str(item.year), item.median_age,
                ])

        context['wp_chart'] = json.dumps(
            wp_chart, cls=LazyEncoder)
        context['wp_future_chart'] = json.dumps(
            wp_future_chart, cls=LazyEncoder)

        context['wp_chart_growth'] = json.dumps(
            wp_chart_growth, cls=LazyEncoder)
        context['wp_future_chart_growth'] = json.dumps(
            wp_future_chart_growth, cls=LazyEncoder)

        context['wp_chart_density'] = json.dumps(
            wp_chart_density, cls=LazyEncoder)
        context['wp_future_chart_density'] = json.dumps(
            wp_future_chart_density, cls=LazyEncoder)

        context['wp_chart_fertility'] = json.dumps(
            wp_chart_fertility, cls=LazyEncoder)
        context['wp_future_chart_fertility'] = json.dumps(
            wp_future_chart_fertility, cls=LazyEncoder)

        context['wp_chart_median_age'] = json.dumps(
            wp_chart_median_age, cls=LazyEncoder)
        context['wp_future_chart_median_age'] = json.dumps(
            wp_future_chart_median_age, cls=LazyEncoder)

        context['population'] = wp

        return context


class WorldPopulationDetailView(TemplateView):
    """"""

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['year'] = current_year
        context['year_title'] = titles['year']
        context['title'] = titles['world']
        context['title_page_prefix'] = titles['pop']
        context['growth_rate'] = titles['growth_rate']
        context['median_age'] = titles['median_age']
        context['density'] = titles['density']
        context['fertility'] = titles['fertility_rate']

        population = WorldPopulation.objects.all()
        wp = population.filter(year__lte=current_year)

        wp_future = population.filter(year__in=years_future)

        wp_chart = [
            # [
            #     titles['year'], titles['total'],
            #     titles['female'], titles['male'],
            # ]
        ]

        wp_chart_growth = [
            [
                titles['year'], titles['growth_rate'],
            ]
        ]
        wp_chart_density = [
            [
                titles['year'], titles['density'],
            ]
        ]
        wp_chart_fertility = [
            [
                titles['year'], titles['fertility_rate'],
            ]
        ]
        wp_chart_median_age = [
            [
                titles['year'], titles['median_age'],
            ]
        ]

        wp_future_chart = [
            # [
            #     titles['year'], titles['total'],
            #     titles['female'], titles['male'],
            # ]
        ]

        wp_future_chart_growth = [
            [
                titles['year'], titles['growth_rate'],
            ]
        ]
        wp_future_chart_density = [
            [
                titles['year'], titles['density'],
            ]
        ]
        wp_future_chart_fertility = [
            [
                titles['year'], titles['fertility_rate'],
            ]
        ]
        wp_future_chart_median_age = [
            [
                titles['year'], titles['median_age'],
            ]
        ]

        for idx, item in enumerate(wp):
            wp_chart.append([
                str(item.year), item.total,
                item.female, item.male
            ])
            wp_chart_growth.append([
                str(item.year), item.change_rate,
            ])
            wp_chart_density.append([
                str(item.year), item.density,
            ])
            if (idx+1) % 5 == 0:
                wp_chart_fertility.append([
                    str(item.year), item.fertility_rate,
                ])
                wp_chart_median_age.append([
                    str(item.year), item.median_age,
                ])

        for item in wp_future:
            wp_future_chart.append([
                str(item.year), item.total,
                item.female, item.male
            ])
            wp_future_chart_growth.append([
                str(item.year), item.change_rate,
            ])
            wp_future_chart_density.append([
                str(item.year), item.density,
            ])
            wp_future_chart_fertility.append([
                str(item.year), item.fertility_rate,
            ])
            wp_future_chart_median_age.append([
                str(item.year), item.median_age,
            ])

        context['wp_chart'] = json.dumps(
            wp_chart, cls=LazyEncoder)
        context['wp_future_chart'] = json.dumps(
            wp_future_chart, cls=LazyEncoder)

        context['wp_chart_growth'] = json.dumps(
            wp_chart_growth, cls=LazyEncoder)
        context['wp_future_chart_growth'] = json.dumps(
            wp_future_chart_growth, cls=LazyEncoder)
        context['wp_chart_density'] = json.dumps(
            wp_chart_density, cls=LazyEncoder)
        context['wp_future_chart_density'] = json.dumps(
            wp_future_chart_density, cls=LazyEncoder)
        context['wp_chart_fertility'] = json.dumps(
            wp_chart_fertility, cls=LazyEncoder)
        context['wp_future_chart_fertility'] = json.dumps(
            wp_future_chart_fertility, cls=LazyEncoder)
        context['wp_chart_median_age'] = json.dumps(
            wp_chart_median_age, cls=LazyEncoder)
        context['wp_future_chart_median_age'] = json.dumps(
            wp_future_chart_median_age, cls=LazyEncoder)

        context['population'] = wp

        context['countries_population'] = \
            CountryPopulation.objects.\
            filter(year=current_year, total__isnull=False).\
            order_by('total').select_related('country')

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
        context['title_page_prefix'] = titles['pop']
        return context
