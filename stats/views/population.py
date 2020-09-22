import json

from django.db.models import Q
from django.template import RequestContext
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, ListView, TemplateView

from core.choices import current_year, titles, years_future
from core.utils import LazyEncoder
from places.models import Country
from stats.models import (
    CountryPopulation, WorldPopulation,
)
from stats.services import get_population


class CountryPopulationDetailView(TemplateView):
    """"""
    slug_field = 'country__slug'
    slug_url_kwarg = 'country_slug'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['stats_type'] = 'pop'
        context['title'] = Country.objects.filter(
            slug=self.kwargs['country_slug'])[0]
        context['title_page_prefix'] = titles['pop']
        context['year_title'] = titles['year']
        context['growth_rate'] = titles['growth_rate']
        context['median_age'] = titles['median_age']
        context['density'] = titles['density']
        context['fertility'] = titles['fertility_rate']

        population_all = CountryPopulation.objects.filter(
            country__slug=self.kwargs['country_slug']).\
            order_by('year').select_related('country')

        population = population_all.filter(year__lte=current_year)

        pop_future = population_all.filter(year__in=years_future)

        pop_chart = [
            # [
            #     titles['year'], titles['total'],
            #     titles['female'], titles['male'],
            # ]
        ]

        pop_chart_growth = [
            [
                titles['year'], titles['growth_rate'],
            ]
        ]
        pop_chart_density = [
            [
                titles['year'], titles['density'],
            ]
        ]
        pop_chart_fertility = [
            # [
            #     titles['year'], titles['fertility_rate'],
            # ]
        ]
        pop_chart_median_age = [
            # [
            #     titles['year'], titles['median_age'],
            # ]
        ]

        pop_future_chart = [
            # [
            #     titles['year'], titles['total'],
            #     titles['female'], titles['male'],
            # ]
        ]

        pop_future_chart_growth = [
            [
                titles['year'], titles['growth_rate'],
            ]
        ]
        pop_future_chart_density = [
            [
                titles['year'], titles['density'],
            ]
        ]
        pop_future_chart_fertility = [
            # [
            #     titles['year'], titles['fertility_rate'],
            # ]
        ]
        pop_future_chart_median_age = [
            # [
            #     titles['year'], titles['median_age'],
            # ]
        ]

        for idx, item in enumerate(population):
            pop_chart.append([
                str(item.year), item.total,
                item.female, item.male
            ])
            pop_chart_growth.append([
                str(item.year), item.change_rate,
            ])
            pop_chart_density.append([
                str(item.year), item.density,
            ])
            if (idx+1) % 5 == 0:
                if item.fertility_rate:
                    pop_chart_fertility.append([
                        str(item.year), item.fertility_rate,
                    ])
                if item.median_age:
                    pop_chart_median_age.append([
                        str(item.year), item.median_age,
                    ])

        for item in pop_future:
            pop_future_chart.append([
                str(item.year), item.total,
                item.female, item.male
            ])
            pop_future_chart_growth.append([
                str(item.year), item.change_rate,
            ])
            pop_future_chart_density.append([
                str(item.year), item.density,
            ])
            if item.fertility_rate:
                pop_future_chart_fertility.append([
                    str(item.year), item.fertility_rate,
                ])
            if item.median_age:
                pop_future_chart_median_age.append([
                    str(item.year), item.median_age,
                ])

        context['pop_chart'] = json.dumps(
            pop_chart, cls=LazyEncoder)
        context['pop_future_chart'] = json.dumps(
            pop_future_chart, cls=LazyEncoder)

        context['pop_chart_growth'] = json.dumps(
            pop_chart_growth, cls=LazyEncoder)
        context['pop_future_chart_growth'] = json.dumps(
            pop_future_chart_growth, cls=LazyEncoder)

        context['pop_chart_density'] = json.dumps(
            pop_chart_density, cls=LazyEncoder)
        context['pop_future_chart_density'] = json.dumps(
            pop_future_chart_density, cls=LazyEncoder)

        context['pop_chart_fertility'] = json.dumps(
            pop_chart_fertility, cls=LazyEncoder)
        context['pop_future_chart_fertility'] = json.dumps(
            pop_future_chart_fertility, cls=LazyEncoder)

        context['pop_chart_median_age'] = json.dumps(
            pop_chart_median_age, cls=LazyEncoder)
        context['pop_future_chart_median_age'] = json.dumps(
            pop_future_chart_median_age, cls=LazyEncoder)

        context['population'] = population

        return context


class WorldPopulationDetailView(TemplateView):
    """"""

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['stats_type'] = 'pop'
        context['year'] = current_year
        context['year_title'] = titles['year']
        context['title'] = titles['world']
        context['title_page_prefix'] = titles['pop']
        context['growth_rate'] = titles['growth_rate']
        context['median_age'] = titles['median_age']
        context['density'] = titles['density']
        context['fertility'] = titles['fertility_rate']

        population_all = WorldPopulation.objects.all()
        population = population_all.filter(year__lte=current_year)

        pop_future = population_all.filter(year__in=years_future)

        pop_chart = [
            # [
            #     titles['year'], titles['total'],
            #     titles['female'], titles['male'],
            # ]
        ]

        pop_chart_growth = [
            [
                titles['year'], titles['growth_rate'],
            ]
        ]
        pop_chart_density = [
            [
                titles['year'], titles['density'],
            ]
        ]
        pop_chart_fertility = [
            [
                titles['year'], titles['fertility_rate'],
            ]
        ]
        pop_chart_median_age = [
            [
                titles['year'], titles['median_age'],
            ]
        ]

        pop_future_chart = [
            # [
            #     titles['year'], titles['total'],
            #     titles['female'], titles['male'],
            # ]
        ]

        pop_future_chart_growth = [
            [
                titles['year'], titles['growth_rate'],
            ]
        ]
        pop_future_chart_density = [
            [
                titles['year'], titles['density'],
            ]
        ]
        pop_future_chart_fertility = [
            [
                titles['year'], titles['fertility_rate'],
            ]
        ]
        pop_future_chart_median_age = [
            [
                titles['year'], titles['median_age'],
            ]
        ]

        for idx, item in enumerate(population):
            pop_chart.append([
                str(item.year), item.total,
                item.female, item.male
            ])
            pop_chart_growth.append([
                str(item.year), item.change_rate,
            ])
            pop_chart_density.append([
                str(item.year), item.density,
            ])
            if (idx+1) % 5 == 0:
                pop_chart_fertility.append([
                    str(item.year), item.fertility_rate,
                ])
                pop_chart_median_age.append([
                    str(item.year), item.median_age,
                ])

        for item in pop_future:
            pop_future_chart.append([
                str(item.year), item.total,
                item.female, item.male
            ])
            pop_future_chart_growth.append([
                str(item.year), item.change_rate,
            ])
            pop_future_chart_density.append([
                str(item.year), item.density,
            ])
            pop_future_chart_fertility.append([
                str(item.year), item.fertility_rate,
            ])
            pop_future_chart_median_age.append([
                str(item.year), item.median_age,
            ])

        context['pop_chart'] = json.dumps(
            pop_chart, cls=LazyEncoder)
        context['pop_future_chart'] = json.dumps(
            pop_future_chart, cls=LazyEncoder)

        context['pop_chart_growth'] = json.dumps(
            pop_chart_growth, cls=LazyEncoder)
        context['pop_future_chart_growth'] = json.dumps(
            pop_future_chart_growth, cls=LazyEncoder)
        context['pop_chart_density'] = json.dumps(
            pop_chart_density, cls=LazyEncoder)
        context['pop_future_chart_density'] = json.dumps(
            pop_future_chart_density, cls=LazyEncoder)
        context['pop_chart_fertility'] = json.dumps(
            pop_chart_fertility, cls=LazyEncoder)
        context['pop_future_chart_fertility'] = json.dumps(
            pop_future_chart_fertility, cls=LazyEncoder)
        context['pop_chart_median_age'] = json.dumps(
            pop_chart_median_age, cls=LazyEncoder)
        context['pop_future_chart_median_age'] = json.dumps(
            pop_future_chart_median_age, cls=LazyEncoder)

        context['population'] = population

        context['countries_population'] = \
            CountryPopulation.objects.\
            filter(year=current_year, total__isnull=False).\
            order_by('total').select_related('country')

        return context
