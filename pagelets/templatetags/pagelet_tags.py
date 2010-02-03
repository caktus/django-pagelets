import copy

from django import template
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.utils.encoding import smart_str
from django.template import Node, NodeList, Variable, Library, Context
from django.template import TemplateSyntaxError, VariableDoesNotExist
from django.core.urlresolvers import reverse

from pagelets.models import Pagelet, Page

register = template.Library()

@register.inclusion_tag('pagelets/_render_pagelet.html', takes_context=True)
def render_pagelet(context, pagelet):
    """
    Renders the named pagelet in the calling template.
    """
    # don't modify the parent context
    context = Context({'request': context['request'], 'perms': context['perms']})
    if isinstance(pagelet, basestring):
        # add the slug separately because we need it in the template even
        # if this pagelet doesn't exist
        context['pagelet_slug'] = pagelet
        try:
            pagelet = Pagelet.objects.get(slug=pagelet)
        except Pagelet.DoesNotExist:
            pagelet = None
    
    if pagelet:
        # add the slug separately because we need it in the template even
        # if this pagelet doesn't exist
        context['pagelet_slug'] = pagelet.slug
        pagelet.rendered_content = pagelet.render(context)
        
    context['pagelet'] = pagelet
    return context


@register.inclusion_tag('pagelets/_pagelink_ifexists.html', takes_context=True)
def pagelink_ifexists(context, page, link_text):
    """
    Renders a link to the given page in the calling template.
    """
    # don't modify the parent context
    context = Context({})
    if isinstance(page, basestring):
        # add the slug separately because we need it in the template even
        # if this page doesn't exist
        context['page_slug'] = page
        try:
            page = Page.objects.get(slug=page)
        except Page.DoesNotExist:
            page = None
    
    if page:
        # add the slug separately because we need it in the template even
        # if this page doesn't exist
        context['page_slug'] = page.slug
        
    context['page'] = page
    context['link_text'] = link_text
    return context
