from django.urls import path
from . import views
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticSitemap, CategorySitemap

sitemaps = {
    'static': StaticSitemap,
    'categories': CategorySitemap
}


urlpatterns = [
    path('', views.home, name="home"),
    path('test', views.test, name="test"),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap')
]
