import hashlib

from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from django.views.decorators.http import condition
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.db.models import Max

from pagelets.models import Pagelet, InlinePagelet, Page, PageAttachment
from pagelets.forms import PageletForm, UploadForm
from pagelets import conf


def view_page(request, page_slug, template='pagelets/view_page.html'):
    page = get_object_or_404(Page, slug=page_slug)

    context = {
        'page': page,
    }
    return render_to_response(
        page.base_template or template,
        context,
        context_instance=RequestContext(request),
    )


@user_passes_test(lambda u: u.has_perm('pagelets.add_pagelet'),
                  login_url=settings.LOGIN_URL)
def create_pagelet(request, pagelet_slug=None):
    page = None
    if 'page_id' in request.GET:
        try:
            page_id = int(request.GET['page_id'])
            page = Page.objects.get(pk=page_id)
        except (Page.DoesNotExist, ValueError):
            pass
    content_area = ''
    if 'content_area' in request.GET and\
       request.GET['content_area'] in [slug for slug, name in conf.CONTENT_AREAS]:
        content_area = request.GET['content_area']
    pagelet = None
    if pagelet_slug:
        try:
            pagelet = Pagelet.objects.get(slug=pagelet_slug)
        except Pagelet.DoesNotExist:
            pass
    if not pagelet:
        order = None
        if page:
            # if the page exists, set the order of this pagelet to
            # max(page.inline_pagelets.order) + 1
            order = page.inline_pagelets.aggregate(Max('order'))['order__max'] or 0
            order += 1
            pagelet = InlinePagelet.objects.create(
                slug=pagelet_slug or '',
                created_by=request.user,
                modified_by=request.user,
                page=page,
                area=content_area,
                order=order,
            )
        else:
            pagelet = Pagelet.objects.create(
                slug=pagelet_slug or '',
                created_by=request.user,
                modified_by=request.user,
            )
    edit_pagelet = reverse('edit_pagelet', kwargs={'pagelet_id': pagelet.id})
    if 'next' in request.GET:
        edit_pagelet += '?next=%s' % request.GET['next']
    return HttpResponseRedirect(edit_pagelet)


def _last_modified(request, pagelet_id):
    pagelet = get_object_or_404(Pagelet, pk=pagelet_id)
    return pagelet.last_changed


def _etag(request, pagelet_id):
    pagelet = get_object_or_404(Pagelet, pk=pagelet_id)
    etag = hashlib.md5(str(sorted(vars(pagelet).items())).encode('utf8')).hexdigest()
    return etag


@condition(last_modified_func=_last_modified, etag_func=_etag)
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

    @user_passes_test(
        lambda u: u.has_perm('pagelets.change_pagelet'),
        login_url=settings.LOGIN_URL)
    def _(request):
        preview_form = None
        pagelet_preview = None
        if request.POST:
            form = PageletForm(request.POST, instance=pagelet)
            if form.is_valid():
                if 'save_btn' in request.REQUEST:
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
    return _(request)


@user_passes_test(lambda u: u.has_perm('pagelets.delete_pagelet'),
                  login_url=settings.LOGIN_URL)
def remove_pagelet(
    request,
    pagelet_id,
    template='pagelets/remove_pagelet.html',
    redirect_field_name=REDIRECT_FIELD_NAME,
    redirect_to=None,
):
    pagelet = get_object_or_404(Pagelet, pk=pagelet_id)

    redirect_to = request.REQUEST.get(redirect_field_name, redirect_to)
    if not redirect_to:
        redirect_to = '/'

    if request.method == 'POST':
        pagelet.delete()
        messages.info(request, 'Pagelet successfully deleted.')
        return HttpResponseRedirect(redirect_to)
    return render_to_response(
        template,
        {'pagelet': pagelet},
        context_instance=RequestContext(request),
    )


@user_passes_test(lambda u: u.has_perm('pagelets.add_pageattachment'),
                  login_url=settings.LOGIN_URL)
def add_attachment(
        request,
        page_slug,
        template='pagelets/attach.html',
):
    page = get_object_or_404(Page, slug=page_slug)
    if request.POST:
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(page=page)
            return HttpResponseRedirect(
                reverse('view_page', args=[page.slug])
            )

    else:
        form = UploadForm()
    context = {
        'page': page,
        'form': form,
    }
    return render_to_response(
        template,
        context,
        context_instance=RequestContext(request),
    )


@user_passes_test(lambda u: u.has_perm('pagelets.delete_pageattachment'),
                  login_url=settings.LOGIN_URL)
def remove_attachment(request, page_slug, attachment_id):
    attachment = get_object_or_404(
        PageAttachment,
        pk=attachment_id,
        page__slug=page_slug,
    )
    attachment.delete()
    if 'next' in request.GET:
        return HttpResponseRedirect(request.GET['next'])
    else:
        return HttpResponseRedirect('/')
