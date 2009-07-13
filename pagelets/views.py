from django import forms
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext, TemplateDoesNotExist
from django.shortcuts import get_object_or_404
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test
from django.template.loader import get_template
from django.core.urlresolvers import reverse

from pagelets.models import Pagelet, Page
from pagelets.forms import PageletForm
from photologue.models import Photo, Gallery


def view_page(request, page_slug, template='pagelets/view_page.html'):
    page = get_object_or_404(Page, slug=page_slug)
    
    context = {
        'page': page,
        'pagelets': page.pagelets.order_by('order'),
    }
    return render_to_response(
        template,
        context,
        context_instance=RequestContext(request),
    )


@user_passes_test(lambda u: u.has_perm('pagelets.add_pagelet'), login_url=settings.LOGIN_URL)
def create_pagelet(request, pagelet_slug):
    try:
        pagelet = Pagelet.objects.get(slug=pagelet_slug)
    except Pagelet.DoesNotExist:
        pagelet = Pagelet.objects.create(
            slug=pagelet_slug,
            created_by=request.user,
            modified_by=request.user,
        )
    edit_pagelet = reverse('edit_pagelet', kwargs={'pagelet_id': pagelet.id})
    return HttpResponseRedirect(edit_pagelet)


@user_passes_test(lambda u: u.has_perm('pagelets.change_pagelet'), login_url=settings.LOGIN_URL)
def edit_pagelet(
    request,
    pagelet_id,
    template='pagelets/edit_pagelet.html',
    redirect_field_name=REDIRECT_FIELD_NAME,
    redirect_to=None,
):
    redirect_to = request.REQUEST.get(redirect_field_name, redirect_to)
    if not redirect_to:
        redirect_to = '/'
    
    pagelet = get_object_or_404(Pagelet, pk=pagelet_id)

    preview_form = None
    pagelet_preview = None
    if request.POST:
        form = PageletForm(request.POST, instance=pagelet)
        if form.is_valid():
            if request.REQUEST.has_key('save_btn'):
                form.save(user=request.user)
                return HttpResponseRedirect(redirect_to)
            else:
                preview_form = PageletForm(
                    request.POST, 
                    instance=pagelet, 
                    preview=True,
                )
                pagelet_preview = form.save(commit=False, user=request.user)
    else:
        form = PageletForm(instance=pagelet)
    
    context = {
        'form': form,
        'pagelet': pagelet,
        'preview_form': preview_form,
        'pagelet_preview': pagelet_preview,
    }
    
    return render_to_response(
        template,
        context,
        context_instance=RequestContext(request),
    )
