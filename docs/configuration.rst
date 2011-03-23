Optional Additional Setup
=========================

Sitemap
-------------------------

If you are using the `contrib.sitemaps` application to generate your sitemap you can make use of the `PageSiteMap`, e.g.::

    from django.conf.urls.defaults import *
    from pagelets.sitemaps import PageSiteMap

    sitemaps = {
        'pagelets': PageSiteMap(priority=0.6),
        # Your other sitemaps
        # ...
    }

    # Site url patterns would go here
    # ...

    urlpatterns += patterns('',

        # the sitemap
        (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    )


Auto template tag loading
-------------------------

To automatically load a custom template tag on every pagelet, add a
``PAGELET_TEMPLATE_TAGS`` list to settings.py::

    PAGELET_TEMPLATE_TAGS = (
        'myapp_tags',
        'myotherapp_tags',
    )


Custom base templates and content areas
---------------------------------------

By default, django-pagelets uses a simplified setup for rendering pages in a
uniform way. However, pages can be modified to extend from different base
templates for greater customization. Pagelets can also specify custom content
areas to allow for special grouping and positioning within pages.

Base templates and content areas can be customized via 2 settings:
PAGELET_BASE_TEMPLATES and PAGELET_CONTENT_AREAS. For example, if you'd like
to add an alternative 2-column layout, you could define the settings like so::

    PAGELET_BASE_TEMPLATES = (
        ('pagelets/two_column_page.html', 'Two Column'),
    )

    PAGELET_CONTENT_AREAS = (
        ('main', 'Main'),
        ('sidebar', 'Sidebar'),
    )

.. highlight:: html+django

The page admin will now include an additional form field to select a base
template and pagelets will allow the specification of content areas. The `Two
Column` template could look something like this::

    {% extends "base.html" %}

    {% load pagelet_tags %}

    {% block title %}{{ page.title }}{% endblock %}

    {% block content %}
        <div id="main-panel">
            {% render_content_area page 'main' %}
        </div>
        <div id="sidebar-panel">
            {% render_content_area page 'sidebar' %}
        </div>
    {% endblock %}

Note the ``render_content_area`` template tags with ``main`` and ``sidebar``
specified.
