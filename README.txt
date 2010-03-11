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

Installation
============
1) Download the app through SVN and add it to your Python path:

    ::

        svn co http://django-pagelets.googlecode.com/svn/trunk/ pagelets

2) Install to dist-packages

    ::

        (sudo) python setup.py install

3) Add to your INSTALLED_APPS and run syncdb

    ::

        INSTALLED_APPS = (
            ...,
            'pagelets',
        )

4) Copy the CSS and, if you need it, the WYMeditor CSS and JavaScript into your static media directory:

    ::

        rsync -av --exclude=.svn pagelets/media/ /path/to/project/media


  If you don't have `rsync`, you can accomplish the same thing by manually copying all the directories within the `pagelets/media` directory into your project's static media directory and removing the `.svn` folders in the target (assuming you got the pagelets app from Subversion).

Setup
=====
1) Add the pagelets tables to your database:

    ::

        ./manage.py syncdb

2) Add the pagelets CSS and, if desired, the WYMeditor CSS/JavaScript to your base.html template:

    ::

        <link rel="stylesheet" href="{{ MEDIA_URL }}css/pagelets.css" />
        <script type="text/javascript" src="{{ MEDIA_URL }}js/jquery-1.3.2.min.js"></script>
        <script type="text/javascript" src="{{ MEDIA_URL }}wymeditor/jquery.wymeditor.min.js"></script>
        <script type="text/javascript" src="{{ MEDIA_URL }}wymeditor/pagelets.js"></script>

3) Add the pagelets URLs to your `urls.py` file, e.g.:

    ::

        (r'^pages/', include('pagelets.urls')),

4) Visit the admin site, add and save a new page, and click the View on site link.  If everything is setup correctly, you should be able to see and edit the content you just added.

Development sponsored by `Caktus Consulting Group, LLC.
<http://www.caktusgroup.com/services>`_.
