from django.conf import settings
from django import forms
from django.utils.translation import gettext_lazy as _

import selectable.forms
from selectable.base import ModelLookup
from selectable.registry import registry
from taggit.models import Tag

from pagelets.models import Page, Pagelet, PageAttachment, get_pagelet_type_assets



class TagLookup(ModelLookup):
    model = Tag
    search_fields = ('name__icontains',)


registry.register(TagLookup)


class PageletForm(forms.ModelForm):

    class Meta:
        model = Pagelet
        fields = ('type', 'content')

    class Media:
        css = {
            'all': ('css/pagelets.css',)
        }
        js = ('js/pagelets.js',)

        js, css = get_pagelet_type_assets(base_scripts=js, base_styles=css)

    def __init__(self, *args, **kwargs):
        self.preview = kwargs.pop('preview', False)
        super(PageletForm, self).__init__(*args, **kwargs)
        if self.preview:
            for field in self.fields.values():
                field.widget = forms.HiddenInput()
        else:
            self.fields['content'].widget = forms.Textarea(
                attrs={'rows': 30, 'cols': 90}
            )

        if len(self.fields['type'].choices) == 1:
            self.fields['type'].widget = forms.HiddenInput()
            self.fields['type'].initial = self.fields['type'].choices[0][0]

    def save(self, commit=True, user=None):
        instance = super(PageletForm, self).save(commit=False)
        if user:
            instance.created_by = user
            instance.modified_by = user
        else:
            raise ValueError(_(u'A user is required when saving a Pagelet'))
        if commit:
            instance.save()
        return instance


class UploadForm(forms.ModelForm):

    class Meta:
        model = PageAttachment
        fields = ('name', 'file', 'order')

    def save(self, page, commit=True):
        instance = super(UploadForm, self).save(commit=False)
        instance.page = page
        if commit:
            instance.save()
        return instance



class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ('title', 'slug', 'tags', 'description', 'meta_keywords', 'meta_robots', 'base_template')

    tags = selectable.forms.AutoCompleteSelectMultipleField(
        lookup_class=TagLookup,
        label='Select a tag',
        required=False,
    )
    base_template = forms.CharField(widget=forms.Select(choices=getattr(settings, 'PAGELET_BASE_TEMPLATES', [])))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.initial['tags'] = self.instance.tags.all().values_list('pk', flat=True)

    def save(self, *args, **kwargs):
        ret = super().save(*args, **kwargs)
        ret._pending_tags = set(tag.name for tag in self.cleaned_data['tags'])
        return ret
