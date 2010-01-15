from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.views.generic.simple import direct_to_template, redirect_to
from django.core.urlresolvers import reverse

from pagelets import views


urlpatterns = patterns('',
    url(
        r'^create/(?:(?P<pagelet_slug>[^/]+)/)?$',
        views.create_pagelet,
        name='create_pagelet',
    ),
    url(
        r'^edit/(?P<pagelet_id>\d+)/$',
        views.edit_pagelet,
        name='edit_pagelet',
    ),
    url(
        r'^remove/(?P<pagelet_id>\d+)/$',
        views.remove_pagelet,
        name='remove_pagelet',
    ),
    url(
        r'^content/(?P<page_slug>[\w-]+)/$',
        views.view_page,
        name='view_page',
    ),
    url(
        r'^content/(?P<page_slug>[\w-]+)/attachment/upload/$',
        views.add_attachment,
        name='add_attachment',
    ),
    url(
        r'^content/(?P<page_slug>[\w-]+)/attachment/(?P<attachment_id>\d+)/remove/$',
        views.remove_attachment,
        name='remove_attachment',
    ),
)
