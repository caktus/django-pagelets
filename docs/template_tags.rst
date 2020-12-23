Built-in Template Tags
======================

.. highlight:: html+django

Render Pagelet
--------------

::

    {% render_pagelet pagelet %}

This takes in either the slug of a pagelet or the pagelet object itself,
then outputs the content of the pagelet along with some divs to wrap the content,
and adds the administration links when a logged in user has permission to edit.

Create Page
-----------

::

    {% create_page "Link Text" %}

Uses the first argument to create the text in the link and builds a simple link
to create a new page based on the current URL.

This is meant to be used on 404s.

Render Content Area
-------------------

::

    {% render_content_area 'content_area_name' %}

This is used to create content areas on the PAGELET_BASE_TEMPLATES.  For more
information see,
:ref:`custom_base_templates`

Pagelink Ifexists
-----------------

::

    {% pagelink_ifexists pagelet %}

Creates a link to the input pagelet (or pagelet with slug) if it exists; otherwise,
it renders nothing.

Page Content Teaser
-------------------

::

    {% page_content_teaser page number_of_words %}

Uses the content from the pagelets related to the page (or page with slug) and
truncates the texts to the number_of_words.

Page Teaser
-----------

::

    {% page_teaser page number_of_words %}

If the page has a description, then it is truncated to the number_of_words and
returned, after removing the HTML.  If there is no description, then the related
pagelets are searched for <p> tags and the inner HTML is combined then truncated.
