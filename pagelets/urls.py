from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.views.generic.simple import direct_to_template, redirect_to
from django.core.urlresolvers import reverse

from pagelets import views


urlpatterns = patterns('',
    url(
        r'^edit/(?P<pagelet_id>\d+)/$',
        views.edit_pagelet,
        name='edit_pagelet',
    ),
    url(
        r'^content/(?P<page_slug>[\w-]+)/$',
        views.view_page,
        name='view_page',
    ),
)
