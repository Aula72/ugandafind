from django import forms
from .models import Content, Refer
from ckeditor.widgets import CKEditorWidget
class MultipleForm(forms.Form):
    action = forms.CharField(max_length=60, widget=forms.HiddenInput())
class ContentForm(forms.Form):
    body = forms.CharField(widget=CKEditorWidget())
    model = Content
    fields = ['title', 'body', 'photo', 'references']

class ReferForm(forms.Form):
    model = Refer
    fields = ['reference']