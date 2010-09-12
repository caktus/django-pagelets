import os

from django.conf import settings
from django.conf.urls.defaults import *

from pagelets.sitemaps import PageSiteMap
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^sample_project/', include('sample_project.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)

import pagelets
path = os.path.join(os.path.dirname(pagelets.__file__), 'media')

urlpatterns += patterns('',
    (
        r'^%spagelets/(?P<path>.*)' % settings.MEDIA_URL.lstrip('/'),
        'django.views.static.serve',
        {'document_root': path, 'show_indexes': True}
    ),
    (
        r'^%s(?P<path>.*)' % settings.MEDIA_URL.lstrip('/'),
        'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}
    ),
)

sitemaps = {
    'pagelets': PageSiteMap(priority=0.6),
}

urlpatterns += patterns('',
    (r'^pagelets-management/', include('pagelets.urls.management')),
    (r'^', include('pagelets.urls.content')),
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
)
