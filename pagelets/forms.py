from django import forms
from django.utils.translation import gettext_lazy as _

from pagelets.models import Pagelet, PageAttachment


class PageletForm(forms.ModelForm):

    class Meta:
        model = Pagelet
        fields = ('type', 'content')

    class Media:
        css = {
            'all': ('css/pagelets.css',)
        }
        js = ('wymeditor/jquery.wymeditor.js',
              'js/pagelets.js')

    def __init__(self, *args, **kwargs):
        self.preview = kwargs.pop('preview', False)
        super(PageletForm, self).__init__(*args, **kwargs)
        if self.preview:
            for field in self.fields.itervalues():
                field.widget = forms.HiddenInput()
        else:
            self.fields['content'].widget = forms.Textarea(
                attrs={'rows': 30, 'cols': 90}
            )

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
