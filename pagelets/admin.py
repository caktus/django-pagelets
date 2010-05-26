from django.contrib import admin
from django.conf import settings

from pagelets import models as pagelets
try:
    from treenav.admin import GenericMenuItemInline
except ImportError:
    GenericMenuItemInline = None


class InlinePageletAdmin(admin.StackedInline):
    model = pagelets.InlinePagelet
    extra = 1
    fk_name = 'page'
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
    extra = 1
    fk_name = 'page'
    fieldsets = (
        (None, {
            'fields': ('pagelet', ('area', 'order'))
        }),
    )


class InlinePageAttachmentAdmin(admin.StackedInline):
    model = pagelets.PageAttachment
    extra = 1
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
    search_fields = ('title',)
    list_filter = ('modified_by',)
    inlines = [InlinePageletAdmin, SharedPageletAdmin, InlinePageAttachmentAdmin]
    optional_fields = ['description', ('meta_keywords', 'meta_robots')]
    if getattr(settings, 'PAGELET_BASE_TEMPLATES', None):
        optional_fields.insert(0, 'base_template')
    fieldsets = (
        (None, {
            'fields': ('title', 'slug',)
        }),
        ('Optional Information', {
            'classes': ('collapse',),
            'fields': optional_fields,
        }),
    )
    if GenericMenuItemInline:
        inlines.insert(0, GenericMenuItemInline)
    
    def save_model(self, request, obj, form, change):
        if not obj.id:
            obj.created_by = request.user
            obj.modified_by = request.user
        obj.save()
    
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
    
    def content_preview(self, obj):
        return obj.content[:25]
    content_preview.short_description = 'content preview'

    def save_model(self, request, obj, form, change):
        if not obj.id:
            obj.created_by = request.user
            obj.modified_by = request.user
        obj.save()
admin.site.register(pagelets.Pagelet, PageletAdmin)
