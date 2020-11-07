from datetime import datetime

from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from core.choices import current_year
from stats.models import (
    CountryGdp, WorldGdp,
    CountryPopulation, WorldPopulation,
    Covid19,
    WorldHdi, CountryHdi
)


class CountryPopulationSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8
    limit = 10000

    def items(self):
        return CountryPopulation.objects.filter(year=2010)

    def lastmod(self, obj):
        return obj.updated_at


class CountryPopulationGrowthRateSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.5
    limit = 10000

    def items(self):
        return CountryPopulation.objects.filter(year=2010).\
            values(
                'country', 'country__slug', 'year',
                'added_at', 'updated_at',
                'change', 'change_rate')

    def lastmod(self, obj):
        if obj['updated_at']:
            return obj['updated_at']
        return obj['added_at']

    def location(self, item):
        return reverse('country-growth-rate-detail', args=[item['country__slug']])


class CountryPopulationMedianAgeSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.5
    limit = 10000

    def items(self):
        return CountryPopulation.objects.filter(year=2010).\
            values(
                'country', 'country__slug', 'year',
                'added_at', 'updated_at',
                'median_age')

    def lastmod(self, obj):
        if obj['updated_at']:
            return obj['updated_at']
        return obj['added_at']

    def location(self, item):
        return reverse('country-median-age-detail', args=[item['country__slug']])


class CountryPopulationDensitySitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.5
    limit = 10000

    def items(self):
        return CountryPopulation.objects.filter(year=2010).\
            values(
                'country', 'country__slug', 'year',
                'added_at', 'updated_at',
                'density')

    def lastmod(self, obj):
        if obj['updated_at']:
            return obj['updated_at']
        return obj['added_at']

    def location(self, item):
        return reverse('country-density-detail', args=[item['country__slug']])


class CountryPopulationFertilitySitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.5
    limit = 10000

    def items(self):
        return CountryPopulation.objects.filter(year=2010).\
            values(
                'country', 'country__slug', 'year',
                'added_at', 'updated_at',
                'fertility_rate')

    def lastmod(self, obj):
        if obj['updated_at']:
            return obj['updated_at']
        return obj['added_at']

    def location(self, item):
        return reverse('country-fertility-detail', args=[item['country__slug']])


class WorldPopulationSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8
    limit = 10000

    def items(self):
        return WorldPopulation.objects.filter(year=2010)

    def lastmod(self, obj):
        return obj.updated_at


class WorldPopulationGrowthRateSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.5
    limit = 10000

    def items(self):
        return WorldPopulation.objects.filter(year=2010).\
            values('year', 'added_at', 'updated_at', 'change_rate')

    def lastmod(self, obj):
        if obj['updated_at']:
            return obj['updated_at']
        return obj['added_at']

    def location(self, item):
        return reverse('world-growth-rate-detail')


class WorldPopulationMedianAgeSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.5
    limit = 10000

    def items(self):
        return WorldPopulation.objects.filter(year=2010).\
            values('year', 'added_at', 'updated_at', 'median_age')

    def lastmod(self, obj):
        if obj['updated_at']:
            return obj['updated_at']
        return obj['added_at']

    def location(self, item):
        return reverse('world-median-age-detail')


class WorldPopulationDensitySitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.5
    limit = 10000

    def items(self):
        return WorldPopulation.objects.filter(year=2010).\
            values('year', 'added_at', 'updated_at', 'density')

    def lastmod(self, obj):
        if obj['updated_at']:
            return obj['updated_at']
        return obj['added_at']

    def location(self, item):
        return reverse('world-density-detail')


class WorldPopulationFertilitySitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.5
    limit = 10000

    def items(self):
        return WorldPopulation.objects.filter(year=2010).\
            values('year', 'added_at', 'updated_at', 'fertility_rate')

    def lastmod(self, obj):
        if obj['updated_at']:
            return obj['updated_at']
        return obj['added_at']

    def location(self, item):
        return reverse('world-fertility-detail')


class CountryGdpSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8
    limit = 10000

    def items(self):
        return CountryGdp.objects.filter(year=2010)

    def lastmod(self, obj):
        if obj.updated_at:
            return obj.updated_at
        return obj.added_at


class CountryHdiSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8
    limit = 10000

    def items(self):
        return CountryHdi.objects.filter(year=2015)

    def lastmod(self, obj):
        if obj.updated_at:
            return obj.updated_at
        return obj.added_at


class WorldGdpSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8
    limit = 10000

    def items(self):
        return WorldGdp.objects.filter(year=2010)

    def lastmod(self, obj):
        if obj.updated_at:
            return obj.updated_at
        return obj.added_at


class CountryCovid19Sitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8
    limit = 10000

    def items(self):
        return Covid19.objects.filter(date=datetime(2020, 2, 11))

    def lastmod(self, obj):
        if obj.updated_at:
            return obj.updated_at
        return obj.added_at


class WorldCovid19Sitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8
    limit = 10000

    def items(self):
        # Return list of url names for views to include in sitemap
        return [
            'world-covid19-detail'
        ]

    def location(self, item):
        return reverse(item)


class WorldHdiSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8
    limit = 10000

    def items(self):
        return WorldHdi.objects.filter(year=2010)

    def lastmod(self, obj):
        if obj.updated_at:
            return obj.updated_at
        return obj.added_at
