try:
    # Django 1.4+
    from django.conf.urls import patterns, url
except ImportError:
    # Django 1.3
    from django.conf.urls.defaults import patterns, url

from pagelets import views
from pagelets.validators import PAGE_SLUG_RE


urlpatterns = patterns('',
    url(
        r'^(?P<page_slug>%s)/$' % PAGE_SLUG_RE,
        views.view_page,
        name='view_page',
    ),
)
