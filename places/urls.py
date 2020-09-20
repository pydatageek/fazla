from django.urls import path
from django.views.generic import RedirectView

from .views import (
    CountryDetailView, CountryListView,
    ContinentDetailView, ContinentListView,
    WorldDetailView,)

template_base = 'lte/'

urlpatterns = [
    # path('country/', CountryListView.as_view(
    #     template_name=template_base+'places/'+'country-list.html'
    # ), name='country-list'),

    path('world/', WorldDetailView.as_view(
        template_name=template_base+'places/'+'world-detail.html'
    ), name='world-detail'),

    path('<slug:slug>/',
         CountryDetailView.as_view(
             template_name=template_base+'places/'+'country-detail.html'
         ), name='country-detail'),
]
