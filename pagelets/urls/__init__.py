try:
    # Django 1.4+
    from django.conf.urls import include, patterns, url
except ImportError:
    # Django 1.3
    from django.conf.urls.defaults import include, patterns, url

urlpatterns = patterns('',
    url(r'^management/', include('pagelets.urls.management')),
    url(r'^', include('pagelets.urls.content')),
)
