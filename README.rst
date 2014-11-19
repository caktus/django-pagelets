django-pagelets
===============

django-pagelets is a simple, flexible app for integrating static, unstructured content in a Django site.

For complete documentation, checkout `<http://django-pagelets.readthedocs.org>`_

Features
--------

- "Pagelets" for adding small pieces of content to otherwise static templates
- CMS "pages" which include any number of pagelets and, if needed, attachments
- Different pagelet content types including HTML and Markdown
- An integrated WYSIWYG editor (`WYMeditor <http://www.wymeditor.org/>`_) which can be selectively enabled/disabled

Changes in 0.10.0
-----------------

Pagelets 0.10.0 includes a number of changes to support Django 1.7 and the new migration framework.
You should be aware of these changes if you are upgrading from the latest 0.9.x release of pagelets.
If you are using pagelets in a project for the first time with version 0.10.0 or newer, you should
not need to worry about any of these changes.

Pagelets no longer users django-tagging, which did not support Django 1.7 migrations and is no
longer maintained. We now use django-taggit. At the moment there is no migration to move tags from
django-tagging to django-taggit.

Required Dependencies
---------------------

- Django 1.7
- Python 2.7 or 3.3
- Django admin site
- django-taggit 0.12.1 or greater
- django-selectable 0.9.0 or greater
- The `django.core.context_processors.request` context processor

Optional Dependencies
---------------------

- `jQuery 1.7 <http://jquery.com>`_
- `WYMeditor <http://www.wymeditor.org/>`_ (included in pagelets media)

Support for Django 1.4 through 1.6
----------------------------------

If you require support for a Django release before 1.7, you can use a release from the 0.9
line of Pagelets, which supports Django 1.3, 1.4, 1.5, and 1.6. This release is also compatible
with Python 3.3 for appropriate Django versions. At this time we will continue to support security
updates to this version of Pagelets.


Installation and Setup
----------------------

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
        "django.core.context_processors.static",
        "django.contrib.messages.context_processors.messages",
        "django.core.context_processors.request", # <----
    )

#. Add the pagelets URLs to urls.py, e.g.::

    urlpatterns += patterns('',
        url(r'^selectable/', include('selectable.urls')),
        url(r'^pagelets-management/', include('pagelets.urls.management')),
        url(r'^', include('pagelets.urls.content')),
    )

#. Visit the admin site, add and save a new page, and click the View on site link.  If everything is setup correctly, you should be able to see and edit the content you just added.


Development sponsored by `Caktus Consulting Group, LLC.
<http://www.caktusgroup.com/services>`_.
