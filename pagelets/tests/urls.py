try:
    # Django 1.4+
    from django.conf.urls import include, patterns, url
except ImportError:
    # Django 1.3
    from django.conf.urls.defaults import include, patterns, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^pagelets/', include('pagelets.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
