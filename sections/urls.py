from django.urls import path
from django.views.decorators.cache import cache_page
from django.views.generic import RedirectView

from info.views import InfoDetailView, InfoTemplateView, InfoListView
from places.views import (
    CountryDetailView, CountryListView,
    ContinentDetailView, ContinentListView,
    WorldDetailView,
)
from stats.views import (
    CountryPopulationDetailView,
    WorldPopulationDetailView,
    CountryGdpDetailView, WorldGdpDetailView,
    CountryCovid19DetailView, WorldCovid19DetailView,
    CountryHdiDetailView, WorldHdiDetailView
)
from .views import HomeView, AboutView, ContactView, SourceView

template_base = 'lte/'

urlpatterns = [
    # path('country/', CountryListView.as_view(
    #     template_name=template_base+'places/'+'country-list.html'
    # ), name='country-list'),

    path('about/', cache_page(60 * 60 * 24 * 30 * 3)(AboutView.as_view(
        template_name=template_base+'core/'+'about.html'
    )), name='about'),
    path('contact/', cache_page(60 * 60 * 24 * 30 * 3)(ContactView.as_view(
        template_name=template_base+'core/'+'contact.html'
    )), name='contact'),
    path('sources/', cache_page(60 * 60 * 24 * 30 * 3)(SourceView.as_view(
        template_name=template_base+'core/'+'source-page.html'
    )), name='source-page'),

    # path('misc-admin/add-ranking/',
    #      save_covid19_data, name='add-ranking'),
    # path('misc-admin/', Covid19AdminView.as_view(
    #     template_name=template_base+'stats/'+'misc-admin.html'
    # ), name='misc-admin'),

    path('i/international-phone-codes/',
         cache_page(60 * 60 * 24 * 30 * 3)(InfoTemplateView.as_view(
             template_name=template_base+'info/'+'phone-code-detail.html'
         )), name='phone-code-list'),
    path('i/world-capital-cities/',
         cache_page(60 * 60 * 24 * 30 * 3)(InfoTemplateView.as_view(
             template_name=template_base+'info/'+'capital-city-list.html'
         )), name='capital-city-list'),
    path('i/country-codes-iso-un-fips/',
         cache_page(60 * 60 * 24 * 30 * 3)(InfoTemplateView.as_view(
             template_name=template_base+'info/'+'country-code-detail.html'
         )), name='country-code-list'),
    path('i/country-driving-sides/',
         cache_page(60 * 60 * 24 * 30 * 3)(InfoTemplateView.as_view(
             template_name=template_base+'info/'+'driving-side-detail.html'
         )), name='driving-side-list'),
    path('i/country-surface-areas/',
         cache_page(60 * 60 * 24 * 30 * 3)(InfoTemplateView.as_view(
             template_name=template_base+'info/'+'country-area-detail.html'
         )), name='country-area-list'),
    path('i/international-top-level-domains-tlds/',
         cache_page(60 * 60 * 24 * 30 * 3)(InfoTemplateView.as_view(
             template_name=template_base+'info/'+'country-tld-detail.html'
         )), name='country-tld-list'),
    path('i/country-languages-alphabets/',
         cache_page(60 * 60 * 24 * 30 * 3)(InfoTemplateView.as_view(
             template_name=template_base+'info/'+'country-language-list.html'
         )), name='country-language-list'),
    path('i/country-currencies/',
         cache_page(60 * 60 * 24 * 30 * 3)(InfoTemplateView.as_view(
             template_name=template_base+'info/'+'country-currency-list.html'
         )), name='country-currency-list'),
    path('i/<slug:slug>/',
         cache_page(60 * 60 * 24 * 30 * 3)(InfoDetailView.as_view(
             template_name=template_base+'info/'+'info-detail.html'
         )), name='info-detail'),
    # path('i/', InfoListView.as_view(
    #     template_name=template_base+'info/'+'info-list.html'
    # ), name='info-list'),

    path('world/covid19/',
         cache_page(60 * 60 * 3)(WorldCovid19DetailView.as_view(
             template_name=template_base+'stats/'+'world-covid19-detail.html'
         )), name='world-covid19-detail'),
    path('world/hdi/',
         cache_page(60 * 60 * 24 * 30 * 3)(WorldHdiDetailView.as_view(
             template_name=template_base+'stats/'+'world-hdi-detail.html'
         )), name='world-hdi-detail'),
    path('world/gdp/',
         cache_page(60 * 60 * 24 * 30 * 3)(WorldGdpDetailView.as_view(
             template_name=template_base+'stats/'+'world-gdp-detail.html'
         )), name='world-gdp-detail'),

    path('world/population/growth-rate/',
         cache_page(60 * 60 * 24 * 30 * 3)(WorldPopulationDetailView.as_view(
             template_name=template_base+'stats/'+'world-growth-rate-detail.html'
         )), name='world-growth-rate-detail'),
    path('world/population/density/',
         cache_page(60 * 60 * 24 * 30 * 3)(WorldPopulationDetailView.as_view(
             template_name=template_base+'stats/'+'world-density-detail.html'
         )), name='world-density-detail'),
    path('world/population/fertility_rate/',
         cache_page(60 * 60 * 24 * 30 * 3)(WorldPopulationDetailView.as_view(
             template_name=template_base+'stats/'+'world-fertility-detail.html'
         )), name='world-fertility-detail'),
    path('world/population/median_age/',
         cache_page(60 * 60 * 24 * 30 * 3)(WorldPopulationDetailView.as_view(
             template_name=template_base+'stats/'+'world-median-age-detail.html'
         )), name='world-median-age-detail'),
    path('world/population/',
         cache_page(60 * 60 * 24 * 30 * 3)(WorldPopulationDetailView.as_view(
             template_name=template_base+'stats/'+'world-population-detail.html'
         )), name='world-population-detail'),
    path('world/',
         cache_page(60 * 60 * 3)(WorldDetailView.as_view(
             template_name=template_base+'places/'+'world-detail.html'
         )), name='world-detail'),


    path('<str:country_slug>/covid19/',
         cache_page(60 * 60 * 3)(CountryCovid19DetailView.as_view(
             template_name=template_base+'stats/'+'country-covid19-detail.html'
         )), name='country-covid19-detail'),

    path('<str:country_slug>/hdi/',
         cache_page(60 * 60 * 24 * 30 * 3)(CountryHdiDetailView.as_view(
             template_name=template_base+'stats/'+'country-hdi-detail.html'
         )), name='country-hdi-detail'),

    path('<str:country_slug>/gdp/',
         cache_page(60 * 60 * 24 * 30 * 3)(CountryGdpDetailView.as_view(
             template_name=template_base+'stats/'+'country-gdp-detail.html'
         )), name='country-gdp-detail'),

    path('<str:country_slug>/population/growth-rate/',
         cache_page(60 * 60 * 24 * 30 * 3)(CountryPopulationDetailView.as_view(
             template_name=template_base+'stats/'+'country-growth-rate-detail.html'
         )), name='country-growth-rate-detail'),
    path('<str:country_slug>/population/density/',
         cache_page(60 * 60 * 24 * 30 * 3)(CountryPopulationDetailView.as_view(
             template_name=template_base+'stats/'+'country-density-detail.html'
         )), name='country-density-detail'),
    path('<str:country_slug>/population/fertility_rate/',
         cache_page(60 * 60 * 24 * 30 * 3)(CountryPopulationDetailView.as_view(
             template_name=template_base+'stats/'+'country-fertility-detail.html'
         )), name='country-fertility-detail'),
    path('<str:country_slug>/population/median_age/',
         cache_page(60 * 60 * 24 * 30 * 3)(CountryPopulationDetailView.as_view(
             template_name=template_base+'stats/'+'country-median-age-detail.html'
         )), name='country-median-age-detail'),
    path('<str:country_slug>/population/',
         cache_page(60 * 60 * 24 * 30 * 3)(CountryPopulationDetailView.as_view(
             template_name=template_base+'stats/'+'country-population-detail.html'
         )), name='country-population-detail'),
    path('<slug:slug>/',
         cache_page(60 * 60 * 3)(CountryDetailView.as_view(
             template_name=template_base+'places/'+'country-detail.html'
         )), name='country-detail'),

    path('',
         cache_page(60 * 60 * 3)(WorldDetailView.as_view(
             template_name=template_base+'places/'+'world-detail.html'
         )), name='home'),
    # path('', RedirectView.as_view(
    #     url='world/', permanent=False), name='home'),
    # path('', HomeView.as_view(
    #     template_name=template_base+'index.html'
    # ), name='home'),
]
