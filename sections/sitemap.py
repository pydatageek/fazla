from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class HomeSitemap(Sitemap):
    """Reverse 'static' views for XML sitemap."""
    changefreq = "daily"
    priority = 1

    def items(self):
        # Return list of url names for views to include in sitemap
        return [
            'home']

    def location(self, item):
        return reverse(item)


class InfoSitemap(Sitemap):
    """Reverse 'static' views for XML sitemap."""
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        # Return list of url names for views to include in sitemap
        return [
            'phone-code-list', 'capital-city-list', 'country-code-list',
            'driving-side-list', 'country-area-list', 'country-tld-list',
            'country-language-list', 'country-currency-list']

    def location(self, item):
        return reverse(item)


class PageSitemap(Sitemap):
    """Reverse 'static' views for XML sitemap."""
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        # Return list of url names for views to include in sitemap
        return [
            'about', 'contact', 'source-page'
        ]

    def location(self, item):
        return reverse(item)
