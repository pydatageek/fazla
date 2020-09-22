import json

from django.db.models import Q, Prefetch
from django.urls import resolve
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, ListView, TemplateView

from core.choices import titles
from core.utils import LazyEncoder
from economics.models import Currency
from linguistics.models import Alphabet, Language
from places.models import Country
from info.models import Info

# table_caption
# table ths and tds


class InfoTemplateView(TemplateView):
    """"""

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        current_url = resolve(self.request.path_info).url_name

        slug = ''
        title = ''

        country_list = Country.objects.exclude(
            Q(is_alive=False) | Q(iso2='00')).order_by('name')

        if (current_url == 'phone-code-list'):
            slug = 'international-phone-codes'
            title = _('International Phone Codes')
        elif current_url == 'country-code-list':
            slug = 'country-codes-iso-un-fips'
            title = _('Country Codes (ISO, UN, FIPS)')
        elif current_url == 'driving-side-list':
            slug = 'country-driving-sides'
            title = _('Countries Driving Sides')
        elif current_url == 'country-area-list':
            slug = 'country-surface-areas'
            title = _('Country Surface Areas')
            country_list = country_list.order_by('-area')
        elif current_url == 'country-tld-list':
            slug = 'international-top-level-domains-tlds'
            title = _('International Top Level Domains (TLDs)')
        elif current_url == 'capital-city-list':
            slug = 'world-capital-cities'
            title = _('List of all Capital Cities in the World')
        elif current_url == 'country-language-list':
            slug = 'country-languages-alphabets'
            title = _(
                'Spoken Languages and Alphabets in Each Country of the World')
            country_list = country_list.prefetch_related(
                Prefetch(
                    'languages',
                    Language.objects.only('name', 'code')),
                Prefetch(
                    'alphabets',
                    Alphabet.objects.only('name', 'code')),
            )
        elif current_url == 'country-currency-list':
            slug = 'country-currencies'
            title = _('Currencies by Countries')
            country_list = country_list.prefetch_related(
                Prefetch(
                    'currencies',
                    Currency.objects.only('name', 'iso3')),
            )
        else:
            slug = ''

        # country_list = Country.objects.exclude(
        #     Q(is_alive=False) | Q(iso2='00'))

        driving_chart = [
            [
                titles['country'], _('Diriving Side'),
            ]
        ]
        v = 'v'
        f = 'f'
        for idx, item in enumerate(country_list):
            driving_chart.append([
                {v: str(item.name), f: str(item.iso2)
                 }, item.get_driving_side_display()
            ])

        # context['object'] = Info.objects.filter(slug=slug).first()
        context['object_list'] = country_list
        context['title'] = title
        context['title_page_prefix'] = _('Info')

        context['driving_chart'] = json.dumps(
            driving_chart, cls=LazyEncoder)

        return context


class InfoDetailView(DetailView):
    """"""
    model = Info

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        current_url = resolve(self.request.path_info).url_name

        context['title'] = self.object.name
        context['title_page_prefix'] = _('Info')
        return context


class InfoListView(ListView):
    """"""
    model = Info

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = _('Info')
        return context
