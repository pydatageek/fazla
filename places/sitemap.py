from django.contrib.sitemaps import Sitemap

from .models import Country, World


class CountrySitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9
    limit = 10000

    def items(self):
        return Country.objects.filter(is_alive=True)

    def lastmod(self, obj):
        if obj.updated_at:
            return obj.updated_at
        return obj.added_at


class WorldSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9
    limit = 10000

    def items(self):
        return World.objects.filter(place_type='WOR')

    def lastmod(self, obj):
        if obj.updated_at:
            return obj.updated_at
        return obj.added_at
