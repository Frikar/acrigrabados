from django.contrib import sitemaps
from django.urls import reverse
from services.models import Category


class StaticSitemap(sitemaps.Sitemap):
    """Reverse 'static' views for XML sitemap."""
    changefreq = "daily"
    priority = 0.5

    def items(self):
        # Return list of url names for views to include in sitemap
        return ['home', 'contact', 'services']

    def location(self, item):
        return reverse(item)


class CategorySitemap(sitemaps.Sitemap):
    changefreq = "daily"
    priority = 0.8

    def items(self):
        return Category.objects.filter(image__isnull=False)
