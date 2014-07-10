from django.contrib import admin
from django.conf import settings
from django.utils.html import strip_tags
from django import forms

from pagelets.forms import PageForm, InlinePageletForm, SharedPageletForm, PageletForm
from pagelets.utils import truncate_html_words
from pagelets import models as pagelets
if 'treenav' in settings.INSTALLED_APPS:
    from treenav.admin import GenericMenuItemInline
else:
    GenericMenuItemInline = None


JS_URLS = [
    'wymeditor/jquery.wymeditor.js',
    'js/pagelets.js',
]
for code, name, js, css in settings.PAGELET_CONTENT_TYPES:
    JS_URLS.extend(js)


class InlinePageletAdmin(admin.StackedInline):
    model = pagelets.InlinePagelet
    extra = 0
    fk_name = 'page'
    form = InlinePageletForm
    fieldsets = (
        (None, {
            'fields': ('type', 'content')
        }),
        ('Style and Placement', {
            'classes': ('collapse',),
            'fields': ('css_classes', ('area', 'order')),
        }),
    )


class SharedPageletAdmin(admin.StackedInline):
    model = pagelets.SharedPagelet
    extra = 0
    fk_name = 'page'
    form = SharedPageletForm
    fieldsets = (
        (None, {
            'fields': ('pagelet', ('area', 'order'))
        }),
    )


class InlinePageAttachmentAdmin(admin.StackedInline):
    model = pagelets.PageAttachment
    extra = 0
    fieldsets = (
        (None, {
            'fields': (('name', 'order'), 'file')
        }),
    )


class PageAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'modified_by',
        'last_changed',
        'created_by',
        'creation_date',
    )
    form = PageForm
    search_fields = ('title',)
    list_filter = ('modified_by',)
    prepopulated_fields = {'slug': ('title',)}
    inlines = [InlinePageletAdmin, SharedPageletAdmin,
               InlinePageAttachmentAdmin]
    shown_fields = ['title', 'slug', 'tags']
    optional_fields = ['description', ('meta_keywords', 'meta_robots')]
    if getattr(settings, 'PAGELET_BASE_TEMPLATES', None):
        optional_fields.insert(0, 'base_template')
    fieldsets = (
        (None, {
            'fields': shown_fields,
        }),
        ('Optional Information', {
            'classes': ('collapse',),
            'fields': optional_fields,
        }),
    )
    if GenericMenuItemInline:
        inlines.insert(0, GenericMenuItemInline)

    class Media:
        css = {
            'all': ('css/wymeditor.admin.css',)
        }
        js = JS_URLS

    def save_model(self, request, obj, form, change):
        if not obj.id:
            obj.created_by = request.user
            obj.modified_by = request.user
        obj.save()
        if hasattr(obj, '_pending_tags'):
            obj.tags.set(*obj._pending_tags)

    def save_formset(self, request, form, formset, change):
        pagelets = formset.save(commit=False)
        for pagelet in pagelets:
            pagelet.created_by = request.user
            pagelet.modified_by = request.user
            pagelet.save()
        formset.save_m2m()
admin.site.register(pagelets.Page, PageAdmin)


class PageletAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'slug',
        'type',
        'modified_by',
        'last_changed',
        'created_by',
        'creation_date',
        'content_preview',
    )
    search_fields = ('slug', 'content',)
    list_filter = ('type', 'modified_by', 'last_changed', 'creation_date')
    form = PageletForm

    class Media:
        css = {
            'all': ('css/wymeditor.admin.css',)
        }
        js = JS_URLS

    def content_preview(self, obj):
        return strip_tags(truncate_html_words(obj.content, 5))
    content_preview.short_description = 'content preview'

    def save_model(self, request, obj, form, change):
        if not obj.id:
            obj.created_by = request.user
            obj.modified_by = request.user
        obj.save()
admin.site.register(pagelets.Pagelet, PageletAdmin)
