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

Required Dependencies
---------------------

- Django >= 2.2
- A Python version supported by your chosen Django version
- Django admin site
- django-taggit 0.12.1 or greater
- django-selectable 1.2.1 or greater
- The `django.template.context_processors.request` context processor

Optional Dependencies
---------------------

- `jQuery 1.7 <http://jquery.com>`_
- `WYMeditor <http://www.wymeditor.org/>`_ (included in pagelets media)

Installation and Setup
----------------------

#. django-pagelets is available on `PyPI <http://pypi.python.org/pypi/django-pagelets>`_, so the easiest way to install it is to use `pip <http://pip.openplans.org/>`_::

    pip install django-pagelets

#. Add `pagelets`, `selectable` and `taggit` to INSTALLED_APPS in settings.py and run migrate::

        INSTALLED_APPS = (
            ...,
            'pagelets',
            'selectable',
            'taggit'
            ...
        )

#. Make sure `django.template.context_processors.request` is loaded and that you have a template
   directory with a "base.html" template in it::


     TEMPLATES=[
         {
             ...
             'DIRS': ['/home/user/projects/myproject/templates'], # <- should have 'base.html' inside
             ...
             'OPTIONS': {
                 'context_processors': [
                     ...
                     'django.template.context_processors.request',
                 ]
             },
         },
     ],

#. Add the pagelets URLs to urls.py, e.g.::

    urlpatterns += [
        path('selectable/', include('selectable.urls')),
        path('pagelets-management/', include('pagelets.urls.management')),
        path('/', include('pagelets.urls.content')),
    ]

#. Visit the admin site, add and save a new page, and click the View on site link.  If everything is setup correctly, you should be able to see and edit the content you just added.


Development sponsored by `Caktus Consulting Group, LLC.
<http://www.caktusgroup.com/services>`_.
