from django.conf.urls.defaults import *

from pagelets import views
from pagelets.validators import PAGE_SLUG_RE


urlpatterns = patterns('',
    url(
        r'^pagelet/(?:(?P<pagelet_slug>[^/]+)/)?create/$',
        views.create_pagelet,
        name='create_pagelet',
    ),
    url(
        r'^pagelet/(?P<pagelet_id>\d+)/edit/$',
        views.edit_pagelet,
        name='edit_pagelet',
    ),
    url(
        r'^pagelet/(?P<pagelet_id>\d+)/remove/$',
        views.remove_pagelet,
        name='remove_pagelet',
    ),
    url(
        r'^page/(?P<page_slug>{0})/attachment/upload/$'.format(PAGE_SLUG_RE),
        views.add_attachment,
        name='add_attachment',
    ),
    url(
        r'^page/(?P<page_slug>{0})/attachment/(?P<attachment_id>\d+)/remove/$'.format(PAGE_SLUG_RE),
        views.remove_attachment,
        name='remove_attachment',
    ),
)
