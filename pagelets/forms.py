from datetime import datetime

from django import forms
from django.contrib.formtools.preview import FormPreview
from django.utils.encoding import smart_unicode, force_unicode

from pagelets.models import Pagelet

class PageletForm(forms.ModelForm):
    class Meta:
        model = Pagelet
        fields = ('type', 'content',)
    
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
            raise ValueError('A user is required when saving a Pagelet')
        
        if commit:
            instance.save()
        
        return instance




