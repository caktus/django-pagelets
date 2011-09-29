django-pagelets
===============

Simple, flexible app for integrating static, unstructured content in a Django site

For complete documentation checkout, `<http://django-pagelets.readthedocs.org>`_

Features
--------
- "Pagelets" for adding small pieces of content to otherwise static templates
- CMS "pages" which include any number of pagelets and, if needed, attachments
- Different pagelet content types including HTML and Markdown
- An integrated WYSIWYG editor (`WYMeditor <http://www.wymeditor.org/>`_) which can be selectively enabled/disabled

Required Dependencies
---------------------

- Django admin site
- The `django.core.context_processors.request` context processor

Optional Dependencies
---------------------

- `jQuery 1.3 <http://jquery.com>`_
- `WYMeditor <http://www.wymeditor.org/>`_ (included in pagelets media)


Installation and Setup
----------------------

.. highlight:: python

#. django-pagelets is available on `PyPI <http://pypi.python.org/pypi/django-pagelets>`_, so the easiest way to install it is to use `pip <http://pip.openplans.org/>`_::

    pip install django-pagelets

#. Add `pagelets` to INSTALLED_APPS in settings.py and run syncdb::

        INSTALLED_APPS = (
            ...,
            'pagelets',
            ...
        )

#. Add `django.core.context_processors.request` to TEMPLATE_CONTEXT_PROCESSORS::

    TEMPLATE_CONTEXT_PROCESSORS = (
        "django.contrib.auth.context_processors.auth",
        "django.core.context_processors.debug",
        "django.core.context_processors.i18n",
        "django.core.context_processors.media",
        "django.contrib.messages.context_processors.messages",
        "django.core.context_processors.request", # <----
    )

#. Add the pagelets URLs to urls.py, e.g.::

    urlpatterns += patterns('',
        (r'^pagelets-management/', include('pagelets.urls.management')),
        (r'^', include('pagelets.urls.content')),
    )

#. In development, you can serve pagelet's static media in urls.py::

    import pagelets
    path = os.path.join(os.path.dirname(pagelets.__file__), 'media')

    urlpatterns += patterns('',
        (
            r'^%spagelets/(?P<path>.*)' % settings.MEDIA_URL.lstrip('/'),
            'django.views.static.serve',
            {'document_root': path, 'show_indexes': True}
        ),
    )

#. Visit the admin site, add and save a new page, and click the View on site link.  If everything is setup correctly, you should be able to see and edit the content you just added.

History
-------

0.7.1
*****

* Add Read the Docs reference to README
* Update sample_project to work with Django 1.3
* Use CDN for external jQuery dependencies
* Add migration to install sequences properly on PostgreSQL

0.7.0
*****

* Add docs and publish on Read the Docs
* Update media references to work better with staticfiles
* Make PageletBase an abstract base class
* Begin using South for migrations
* Update sample_project to use Django 1.2

0.6.2
*****

* Remove use of .format() to support earlier versions of Python
* Fix license reference and URL endpoint in setup.py
* Include sample_project in MANIFEST.in
* Update license date

0.6.0
*****

* First official release

Development sponsored by `Caktus Consulting Group, LLC.
<http://www.caktusgroup.com/services>`_.