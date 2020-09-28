from django.urls import path
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
    CountryCovid19DetailView, WorldCovid19DetailView
)
from .views import HomeView, AboutView, ContactView, SourceView

template_base = 'lte/'

urlpatterns = [
    # path('country/', CountryListView.as_view(
    #     template_name=template_base+'places/'+'country-list.html'
    # ), name='country-list'),

    path('about/', AboutView.as_view(
        template_name=template_base+'core/'+'about.html'
    ), name='about'),
    path('contact/', ContactView.as_view(
        template_name=template_base+'core/'+'contact.html'
    ), name='contact'),
    path('sources/', SourceView.as_view(
        template_name=template_base+'core/'+'source-page.html'
    ), name='source-page'),

    path('world/covid19/',
         WorldCovid19DetailView.as_view(
             template_name=template_base+'stats/'+'world-covid19-detail.html'
         ), name='world-covid19-detail'),

    path('i/international-phone-codes/', InfoTemplateView.as_view(
        template_name=template_base+'info/'+'phone-code-detail.html'
    ), name='phone-code-list'),
    path('i/world-capital-cities/', InfoTemplateView.as_view(
        template_name=template_base+'info/'+'capital-city-list.html'
    ), name='capital-city-list'),
    path('i/country-codes-iso-un-fips/', InfoTemplateView.as_view(
        template_name=template_base+'info/'+'country-code-detail.html'
    ), name='country-code-list'),
    path('i/country-driving-sides/', InfoTemplateView.as_view(
        template_name=template_base+'info/'+'driving-side-detail.html'
    ), name='driving-side-list'),
    path('i/country-surface-areas/', InfoTemplateView.as_view(
        template_name=template_base+'info/'+'country-area-detail.html'
    ), name='country-area-list'),
    path('i/international-top-level-domains-tlds/', InfoTemplateView.as_view(
        template_name=template_base+'info/'+'country-tld-detail.html'
    ), name='country-tld-list'),
    path('i/country-languages-alphabets/', InfoTemplateView.as_view(
        template_name=template_base+'info/'+'country-language-list.html'
    ), name='country-language-list'),
    path('i/country-currencies/', InfoTemplateView.as_view(
        template_name=template_base+'info/'+'country-currency-list.html'
    ), name='country-currency-list'),
    path('i/<slug:slug>/', InfoDetailView.as_view(
        template_name=template_base+'info/'+'info-detail.html'
    ), name='info-detail'),
    # path('i/', InfoListView.as_view(
    #     template_name=template_base+'info/'+'info-list.html'
    # ), name='info-list'),


    path('world/gdp/',
         WorldGdpDetailView.as_view(
             template_name=template_base+'stats/'+'world-gdp-detail.html'
         ), name='world-gdp-detail'),

    path('world/population/growth-rate/',
         WorldPopulationDetailView.as_view(
             template_name=template_base+'stats/'+'world-growth-rate-detail.html'
         ), name='world-growth-rate-detail'),
    path('world/population/density/',
         WorldPopulationDetailView.as_view(
             template_name=template_base+'stats/'+'world-density-detail.html'
         ), name='world-density-detail'),
    path('world/population/fertility_rate/',
         WorldPopulationDetailView.as_view(
             template_name=template_base+'stats/'+'world-fertility-detail.html'
         ), name='world-fertility-detail'),
    path('world/population/median_age/',
         WorldPopulationDetailView.as_view(
             template_name=template_base+'stats/'+'world-median-age-detail.html'
         ), name='world-median-age-detail'),
    path('world/population/',
         WorldPopulationDetailView.as_view(
             template_name=template_base+'stats/'+'world-population-detail.html'
         ), name='world-population-detail'),
    path('world/', WorldDetailView.as_view(
        template_name=template_base+'places/'+'world-detail.html'
    ), name='world-detail'),


    path('<str:country_slug>/covid19/',
         CountryCovid19DetailView.as_view(
             template_name=template_base+'stats/'+'country-covid19-detail.html'
         ), name='country-covid19-detail'),

    path('<str:country_slug>/gdp/',
         CountryGdpDetailView.as_view(
             template_name=template_base+'stats/'+'country-gdp-detail.html'
         ), name='country-gdp-detail'),

    path('<str:country_slug>/population/growth-rate/',
         CountryPopulationDetailView.as_view(
             template_name=template_base+'stats/'+'country-growth-rate-detail.html'
         ), name='country-growth-rate-detail'),
    path('<str:country_slug>/population/density/',
         CountryPopulationDetailView.as_view(
             template_name=template_base+'stats/'+'country-density-detail.html'
         ), name='country-density-detail'),
    path('<str:country_slug>/population/fertility_rate/',
         CountryPopulationDetailView.as_view(
             template_name=template_base+'stats/'+'country-fertility-detail.html'
         ), name='country-fertility-detail'),
    path('<str:country_slug>/population/median_age/',
         CountryPopulationDetailView.as_view(
             template_name=template_base+'stats/'+'country-median-age-detail.html'
         ), name='country-median-age-detail'),
    path('<str:country_slug>/population/',
         CountryPopulationDetailView.as_view(
             template_name=template_base+'stats/'+'country-population-detail.html'
         ), name='country-population-detail'),
    path('<slug:slug>/',
         CountryDetailView.as_view(
             template_name=template_base+'places/'+'country-detail.html'
         ), name='country-detail'),

    path('', WorldDetailView.as_view(
        template_name=template_base+'places/'+'world-detail.html'
    ), name='home'),
    # path('', RedirectView.as_view(
    #     url='world/', permanent=False), name='home'),
    # path('', HomeView.as_view(
    #     template_name=template_base+'index.html'
    # ), name='home'),
]
