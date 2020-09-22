from django.urls import path
from django.views.generic import RedirectView

from .views import (
    CountryPopulationDetailView,
    WorldPopulationDetailView)

template_base = 'lte/'

urlpatterns = [
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
]
