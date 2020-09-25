from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import resolve, reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.defaults import server_error
from django.views.generic import (
    DetailView, ListView, TemplateView)
from django.views.generic.edit import FormView

from core.choices import titles
from core.forms import ContactForm


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
    # Fazla.net facts and stats


class SourceView(TemplateView):
    """"""

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = _('Sources')
        return context


class AboutView(TemplateView):
    """"""

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = _('About')
        return context


class ContactView(SuccessMessageMixin, FormView):
    """"""
    form_class = ContactForm
    success_url = reverse_lazy('contact')
    success_message = _('Your form submission is successful, thank you.')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = _('Contact Us')
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
