from django.conf.urls.defaults import *

from pagelets import views


urlpatterns = patterns('',
    url(
        r'^(?P<page_slug>[\w-]+)/$',
        views.view_page,
        name='view_page',
    ),
)
