import re

from django import template
from django.core.urlresolvers import reverse
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.template import RequestContext, Context

from pagelets.models import Pagelet, Page, DEFAULT_CONTENT_AREA

register = template.Library()

@register.inclusion_tag('pagelets/_render_pagelet.html', takes_context=True)
def render_pagelet(context, pagelet):
    """
    Renders the named pagelet in the calling template.
    """
    # don't modify the parent context
    parent_context = context
    if 'request' in context:
        context = RequestContext(parent_context['request'])
    else:
        context = Context()
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
        context['page'] = parent_context.get('page', None)
        pagelet.rendered_content = pagelet.render(context)
    context['pagelet'] = pagelet
    context['include_links'] = True
    return context


@register.inclusion_tag('pagelets/_render_content_area.html',
                        takes_context=True)
def render_content_area(context, page, content_area):
    """
    Renders the named content area of the given page in the calling template.
    """
    # don't modify the parent context
    if 'request' in context:
        context = RequestContext(context['request'])
    else:
        context = Context()
    context['page'] = page
    context['content_area'] = content_area
    context['pagelets'] = page.get_area_pagelets(content_area)
    return context


@register.inclusion_tag('pagelets/_pagelink_ifexists.html', takes_context=True)
def pagelink_ifexists(context, page, link_text):
    """
    Renders a link to the given page in the calling template.
    """
    # don't modify the parent context
    if 'request' in context:
        context = RequestContext(context['request'])
    else:
        context = Context()
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


@register.inclusion_tag('pagelets/_page_teaser.html', takes_context=True)
def page_content_teaser(context, page, num_words):
    """
    Renders a teaser of the given page object in the calling template.
    """
    # don't modify the parent context
    if 'request' in context:
        context = RequestContext(context['request'])
    else:
        context = Context()
    if isinstance(page, basestring):
        # add the slug separately because we need it in the template even
        # if this page doesn't exist
        context['page_slug'] = page
        try:
            page = Page.objects.get(slug=page)
        except Pagelet.DoesNotExist:
            page = None
    
    content = ''
    if page:
        # add the slug separately because we need it in the template even
        # if this page doesn't exist
        context['page_slug'] = page.slug
        for pagelet in page.pagelets.order_by('order'):
            pagelet.rendered_content = pagelet.render(context)
            content += render_to_string('pagelets/_render_pagelet.html',
                                        {'include_links': False,
                                         'pagelet': pagelet},
                                        context_instance=context)
    context['page'] = page
    context['content'] = content
    context['num_words'] = num_words
    return context


@register.inclusion_tag('pagelets/_page_teaser_new.html', takes_context=True)    
def page_teaser(context, page, num_words):
    """
    Renders a better teaser of the given page object in the calling template.
    """
    # don't modify the parent context
    if 'request' in context:
        context = RequestContext(context['request'])
    else:
        context = Context()
    if isinstance(page, basestring):
        # add the slug separately because we need it in the template even
        # if this page doesn't exist
        context['page_slug'] = page
        try:
            page = Page.objects.get(slug=page)
        except Pagelet.DoesNotExist:
            page = None
    
    content = ''
    if page:
        # add the slug separately because we need it in the template even
        # if this page doesn't exist
        context['page_slug'] = page.slug
        if page.description:
            content = page.description
        else:
            pagelets = page.get_area_pagelets(DEFAULT_CONTENT_AREA,
                                              with_shared=False)
            pagelets.sort(lambda a, b: len(b.content) - len(a.content))
            for pagelet in pagelets:
                search = re.findall('<p>(.*?)</p>', pagelet.render(context))
                if len(search) != 0:
                    content += ' '.join(search)
                else:
                    content += pagelet.render(context)

    context['page'] = page
    context['content'] = content
    context['num_words'] = num_words
    return context


@register.inclusion_tag('pagelets/_create_page.html', takes_context=True)
def create_page(context, link_text):
    """
    Renders a link to the admin to create a page based on the
    current request path. Meant to be used on a 404 page.
    """
    # don't modify the parent context
    if 'request' in context:
        request = context['request']
        context = RequestContext(request)
    else:
        return {'exists': True}
    
    has_perm = request.user.has_perm('pagelets.add_page')
    

    if has_perm:
        path = request.path.strip('/')
        try:
            exists = Page.objects.filter(slug=path).exists()
        except Page.DoesNotExist:
            exists = False
    else:
        path = ''
        exists = True

    admin_url = reverse('admin:%s_%s_add' % (Page._meta.app_label, Page._meta.module_name))
        
    context['exists'] = exists
    context['admin_url'] = u'{0}?slug={1}'.format(admin_url, path)
    context['link_text'] = link_text
    context['has_perm'] = has_perm
    return context
