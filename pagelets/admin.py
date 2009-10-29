from django.contrib import admin

from pagelets import models as pagelets


class InlinePageletAdmin(admin.StackedInline):
    model = pagelets.Pagelet
    extra = 2
    fk_name = 'page'

class InlinePageAttachmentAdmin(admin.StackedInline):
    model = pagelets.PageAttachment
    
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
    inlines = (InlinePageletAdmin, InlinePageAttachmentAdmin,)
    
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
        'page',
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
