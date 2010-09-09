django-pagelets
===============

Simple, flexible app for integrating static, unstructured content in a Django site

Features
========
  - "Pagelets" for adding small pieces of content to otherwise static templates
  - CMS "pages" which include any number of pagelets and, if needed, attachments
  - Different pagelet content types including HTML and Markdown
  - An integrated WYSIWYG editor (`WYMeditor
    <http://www.wymeditor.org/>`_) which can be selectively enabled/disabled

Dependencies
============
Required
--------
- Django admin site
  - The `django.core.context_processors.request` context processor

Optional
--------
 - `jQuery 1.3
   <http://jquery.com>`_
 - `WYMeditor
   <http://www.wymeditor.org/>`_ (included in pagelets media)

Installation and Setup
======================

1) django-pagelets is available on `PyPI <http://pypi.python.org/pypi/django-pagelets>`_, so the easiest way to install it is to use `pip <http://pip.openplans.org/>`_::

    pip install django-pagelets

2) Add `pagelets` to INSTALLED_APPS in settings.py and run syncdb::

        INSTALLED_APPS = (
            ...,
            'pagelets',
            ...
        )

3) Add the pagelets URLs to urls.py, e.g.::

    urlpatterns += patterns('',
        (r'^pagelets/', include('pagelets.urls.content')),
        (r'^pagelets-management/', include('pagelets.urls.management')),
    )

4) In development, you can serve pagelet's static media in urls.py::

    import pagelets
    path = os.path.join(os.path.dirname(pagelets.__file__), 'media')

    urlpatterns += patterns('',
        (
            r'^%spagelets/(?P<path>.*)' % settings.MEDIA_URL.lstrip('/'),
            'django.views.static.serve',
            {'document_root': path, 'show_indexes': True}
        ),
    )

5) Visit the admin site, add and save a new page, and click the View on site link.  If everything is setup correctly, you should be able to see and edit the content you just added.

Development sponsored by `Caktus Consulting Group, LLC.
<http://www.caktusgroup.com/services>`_.
