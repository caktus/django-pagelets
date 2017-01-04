import os

from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from pagelets.sitemaps import PageSiteMap


admin.autodiscover()
sitemaps = {
    'pagelets': PageSiteMap(priority=0.6),
}


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^pagelets-management/', include('pagelets.urls.management')),
    url(r'^cms/', include('pagelets.urls.content')),
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    url(r'^selectable/', include('selectable.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
