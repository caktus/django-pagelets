import os

from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin

from pagelets.sitemaps import PageSiteMap


admin.autodiscover()
sitemaps = {
    'pagelets': PageSiteMap(priority=0.6),
}


urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^pagelets-management/', include('pagelets.urls.management')),
    (r'^cms/', include('pagelets.urls.content')),
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
)
