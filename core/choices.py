from django.utils import timezone
from django.utils.translation import gettext_lazy as _

current_year = timezone.now().year
years_future = [y for y in range(current_year+1, 2101) if y % 5 == 0]

current_year_gdp = 2019

titles = {
    'year': _('Year'),

    'pop': _('Population'),
    'total': _('Total population'),
    'female': _('Female'),
    'male': _('Male'),

    'growth': _('Growth'),
    'growth_rate': _('Growth Rate'),
    'growth_rate_table': _('Growth %'),

    'fertility_rate': _('Total Fertility'),
    'median_age': _('Median Age'),

    'density': _('Population Density'),
    'density_table': _('Density (people/km2)'),

    'world': _('World'),
    'continent': _('Continent'),
    'country': _('Country'),

    'phone_code': _('International Phone Codes'),
    'country_code': _('Country Codes (ISO, UN, FIPS)'),
    'driving_side': _('Countries Driving Sides'),
    'country_area': _('Country Surface Areas'),
    'country_tld': _('International Top Level Domains (TLDs)'),

    'gdp': _('GDP'),

}
