import json

from django.contrib.auth.decorators import user_passes_test
from django.db.models import F, Q, Window, Value, Subquery
from django.db.models.functions import Rank, DenseRank, Lag
from django.template import RequestContext
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, ListView, TemplateView

from core.choices import titles
from core.utils import LazyEncoder
from places.models import Country
from stats.models import (
    CountryPopulation, CountryGdp, Covid19
)


def check_admin(user):
    return user.is_superuser


def get_covid19_data(country_code):
    """"""


@ user_passes_test(check_admin)
def add_ranking(request):
    """"""
    population = CountryPopulation.objects.all()
    gdp = CountryGdp.objects.all()
    covid19 = Covid19.objects.all()

    # population_rank
    # male_rate_rank
    # female_rate_rank
    # change_rate_rank
    # median_age_rank
    # density_rank

    # gdp_rank
    # gdp_per_capita_rank
    # gdp_ppp_rank
    # gdp_ppp_per_capita_rank
    # gdp_growth_rank

    # new_confirmed_rank
    # new_death_rank
    # total_confirmed_rank
    # total_death_rank


"""
    for idx, country in enumerate(countries):
        print(country.name)
        if idx % 10 == 0:
            time.sleep(60)

        country_data_set = get_covid19_data(country.iso2)

        for i in country_data_set:
            date = i['Date'].split('T')[0]
            date = datetime.strptime(date, '%Y-%m-%d')
            date_temp = date.date()
            # print(country.name)
            # print(latest_date - timedelta(days=2))
            # print(date)
            # if date_temp >= latest_date - timedelta(days=2):
            Covid19.objects.update_or_create(
                country=country,
                province=i['Province'],
                city=i['City'],
                city_code=i['CityCode'],
                latitude=i['Lat'],
                longitude=i['Lon'],
                confirmed=i['Confirmed'],
                death=i['Deaths'],
                recovered=i['Recovered'],
                active=i['Active'],
                date=date
            )
"""


@ method_decorator(user_passes_test(check_admin), name='dispatch')
class MiscAdminView(TemplateView):
    """"""
