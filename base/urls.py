from django.urls import path
from . import views
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticSitemap, CategorySitemap
from django.views.generic.base import TemplateView

sitemaps = {
    'static': StaticSitemap,
    'categories': CategorySitemap
}

urlpatterns = [
    path('', views.home, name="home"),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path("robots.txt", TemplateView.as_view(template_name="robots.txt", content_type="text/plain"))
]
