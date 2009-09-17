
from django import template
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.utils.encoding import smart_str
from django.template import Node, NodeList, Variable, Library
from django.template import TemplateSyntaxError, VariableDoesNotExist
from django.core.urlresolvers import reverse

from pagelets.models import Pagelet, Page

register = template.Library()

@register.inclusion_tag('pagelets/_render_pagelet.html', takes_context=True)
def render_pagelet(context, pagelet, *args):
    """
    Renders the named pagelet in the calling template.
    """
    if isinstance(pagelet, basestring):
        # add the slug separately because we need it in the template even
        # if this pagelet doesn't exist
        context['pagelet_slug'] = pagelet
        context['pagelet_name'] = unicode(pagelet)
        try:
            pagelet = Pagelet.objects.get(slug=pagelet)
        except Pagelet.DoesNotExist:
            pagelet = None
    
    if pagelet:
        # add the slug separately because we need it in the template even
        # if this pagelet doesn't exist
        context['pagelet_slug'] = pagelet.slug
        context['pagelet_name'] = unicode(pagelet)
        pagelet.rendered_content = pagelet.render(context)
        
    context['pagelet'] = pagelet
    if args:
        context['link_text'] = args[0]
    return context


@register.inclusion_tag('pagelets/_pagelink_ifexists.html', takes_context=True)
def pagelink_ifexists(context, page, link_text):
    """
    Renders a link to the given page in the calling template.
    """
    if isinstance(page, basestring):
        # add the slug separately because we need it in the template even
        # if this page doesn't exist
        context['page_slug'] = page
        context['pagelet_name'] = unicode(pagelet)
        try:
            page = Page.objects.get(slug=page)
        except Page.DoesNotExist:
            page = None
    
    if page:
        # add the slug separately because we need it in the template even
        # if this page doesn't exist
        context['page_slug'] = page.slug
        context['pagelet_name'] = unicode(pagelet)
        
    context['page'] = page
    context['link_text'] = link_text
    return context


