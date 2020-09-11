from django.urls import path
from django.views.generic import RedirectView

from .views import (
    HomeView,
    CountryDetailView, CountryListView,
    ContinentDetailView, ContinentListView,
    WorldDetailView,
    InfoDetailView, InfoTemplateView, InfoListView,
    CountryPopulationDetailView,
    InternationalOrganizationPopulationDetailView,
    WorldPopulationDetailView)

template_base = 'lte/'

urlpatterns = [
    # path('country/', CountryListView.as_view(
    #     template_name=template_base+'places/'+'country-list.html'
    # ), name='country-list'),

    path('i/international-phone-codes/', InfoTemplateView.as_view(
        template_name=template_base+'info/'+'phone-code-detail.html'
    ), name='phone-code-list'),
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
    path('i/<slug:slug>/', InfoDetailView.as_view(
        template_name=template_base+'info/'+'info-detail.html'
    ), name='info-detail'),
    path('i/', InfoListView.as_view(
        template_name=template_base+'info/'+'info-list.html'
    ), name='info-list'),


    path('world/population/growth-rate/', WorldPopulationDetailView.as_view(
        template_name=template_base+'stats/'+'world-growth-rate-detail.html'
    ), name='world-growth-rate-detail'),
    path('world/population/density/', WorldPopulationDetailView.as_view(
        template_name=template_base+'stats/'+'world-density-detail.html'
    ), name='world-density-detail'),
    path('world/population/fertility_rate/', WorldPopulationDetailView.as_view(
        template_name=template_base+'stats/'+'world-fertility-detail.html'
    ), name='world-fertility-detail'),
    path('world/population/median_age/', WorldPopulationDetailView.as_view(
        template_name=template_base+'stats/'+'world-median-age-detail.html'
    ), name='world-median-age-detail'),
    path('world/population/', WorldPopulationDetailView.as_view(
        template_name=template_base+'stats/'+'world-population-detail.html'
    ), name='world-population-detail'),
    path('world/', WorldDetailView.as_view(
        template_name=template_base+'places/'+'world-detail.html'
    ), name='world-detail'),



    path('<str:country_slug>/population/growth-rate/', CountryPopulationDetailView.as_view(
        template_name=template_base+'stats/'+'country-growth-rate-detail.html'
    ), name='country-growth-rate-detail'),
    path('<str:country_slug>/population/density/', CountryPopulationDetailView.as_view(
        template_name=template_base+'stats/'+'country-density-detail.html'
    ), name='country-density-detail'),
    path('<str:country_slug>/population/fertility_rate/', CountryPopulationDetailView.as_view(
        template_name=template_base+'stats/'+'country-fertility-detail.html'
    ), name='country-fertility-detail'),
    path('<str:country_slug>/population/median_age/', CountryPopulationDetailView.as_view(
        template_name=template_base+'stats/'+'country-median-age-detail.html'
    ), name='country-median-age-detail'),
    path('<str:country_slug>/population/', CountryPopulationDetailView.as_view(
        template_name=template_base+'stats/'+'country-population-detail.html'
    ), name='country-population-detail'),
    path('<slug:slug>/', CountryDetailView.as_view(
        template_name=template_base+'places/'+'country-detail.html'
    ), name='country-detail'),

    path('o/<str:organization_slug>/population/',
         InternationalOrganizationPopulationDetailView.as_view(
             template_name=template_base+'stats/'+'organization-population-detail.html'
         ), name='organization-population-detail'),



    path('r/c/<slug:slug>/', ContinentDetailView.as_view(
        template_name=template_base+'places/'+'continent-detail.html'
    ), name='continent-detail'),
    path('r/c/', ContinentListView.as_view(
        template_name=template_base+'places/'+'continent-list.html'
    ), name='continent-list'),


    path('', RedirectView.as_view(
        url='world/', permanent=False), name='home'),
    # path('', HomeView.as_view(
    #     template_name=template_base+'index.html'
    # ), name='home'),
]
