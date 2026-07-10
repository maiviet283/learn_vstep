from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.http import HttpResponse
from django.urls import include, path

from learning.sitemaps import (ListeningSitemap, ReadingSitemap,
                               StaticSitemap, UnitSitemap, VocabTopicSitemap)

sitemaps = {
    'static': StaticSitemap,
    'units': UnitSitemap,
    'vocab': VocabTopicSitemap,
    'reading': ReadingSitemap,
    'listening': ListeningSitemap,
}


def robots_txt(request):
    lines = [
        'User-agent: *',
        'Allow: /',
        'Disallow: /admin/',
        '',
        'Sitemap: https://vstep.vietdon.vn/sitemap.xml',
    ]
    return HttpResponse('\n'.join(lines), content_type='text/plain')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('robots.txt', robots_txt),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    path('', include('learning.urls')),
]
