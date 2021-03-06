Release History
====================================

2.0.0 (Released 2020-12-23)
---------------------------
* Add Django 2.2, 3.0 and 3.1 support
* Switch from Travis CI to Github Actions CI
* Add pre-commit, black, isort checks

Breaking changes
~~~~~~~~~~~~~~~~
* Drop Django <2.2 support
* Drop Python 2 support


1.1.0 (Released 2018-04-17)
---------------------------
* Add Django 1.11 support, drop Django <1.11 support

Note: adding Django 2.0 support will require
`django-selectable <http://django-selectable.readthedocs.io/en/latest/>`_
to add Django 2.0 support first.

1.0.0 (Released 2017-01-04)
---------------------------
* Add Django 1.8+ support
* Drop Django 1.7 support
* Travis CI

0.10.0 (Released 2014-11-19)
----------------------------
* Support for Django 1.7
* Moved to django-taggit dropping support for django-tagging
* Dropped South migrations

0.9.1 (Released 2014-11-03)
------------------------------------
* Fixed Python 3 compatibility bug #59
* Removed test coverage for unsupported Python 2.6 and Django 1.3

0.9.0 (Released 2014-02-24)
------------------------------------

* Setup tox
* Support Django's custom user model
* Python 3 support
* Flake8 improvements


0.8.0 (Released 2014-02-05)
------------------------------------

* Fix migrations to run on MySQL
* Configurable content types with included JS/CSS requirements
* Updated message API to be compatible with Django 1.4+
* Updated template url syntax to be compatible with Django 1.5+
* Add missing CSRF token to attach form (see #38)
* Allow use of `{% render_content_area "by-slug-string" %}`
* Provide proper eTag and Last Modified checks to `edit_pagelet` view,
  avoiding edits that get lost by overzealous caching
* Add `truncate_html_words` shim for Django 1.6+ compatibility
* Fix urls.py imports to work with Django 1.6+


0.7.2 (Released 2012-03-28)
------------------------------------

* Updated migration 0003 to be a data migration
* Made Page.tags field always exist, and add migration for it


0.7.1  (Released 2011-09-29)
------------------------------------

* Add Read the Docs reference to README
* Update sample_project to work with Django 1.3
* Use CDN for external jQuery dependencies
* Add migration to install sequences properly on PostgreSQL


0.7.0 (Released 2011-04-01)
------------------------------------

* Add docs and publish on Read the Docs
* Update media references to work better with staticfiles
* Make PageletBase an abstract base class
* Begin using South for migrations
* Update sample_project to use Django 1.2


0.6.2 (Released 2010-12-03)
------------------------------------

* Remove use of .format() to support earlier versions of Python
* Fix license reference and URL endpoint in setup.py
* Include sample_project in MANIFEST.in
* Update license date


0.6.0 (Released 2010-09-12)
------------------------------------

* First official release

Development sponsored by `Caktus Consulting Group, LLC.
<http://www.caktusgroup.com/services>`_.
