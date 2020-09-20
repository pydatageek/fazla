from django.shortcuts import render
from django.urls import resolve
from django.utils.translation import gettext_lazy as _
from django.views.defaults import server_error
from django.views.generic import DetailView, ListView, TemplateView

from core.choices import titles


def handler400(request, exception):
    return render(request, 'lte/400.html', status=400)


def handler403(request, exception):
    return render(request, 'lte/403.html', status=403)


def handler404(request, exception):
    return render(request, 'lte/404.html', status=404)


def handler500(request):
    return server_error(request, 'lte/500.html')


class HomeView(TemplateView):
    """"""
