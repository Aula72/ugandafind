from django import forms
from .models import Contact
# class ContactForm(forms.Form):
#     name = forms.CharField()
#     mail = forms.EmailField(label='E-mail Address')
#     #category = forms.ChoiceField(choices=[('question', 'Question'), ('answer', 'Answer')])
#     subject = forms.CharField(required=False)
#     content = forms.CharField(widget = forms.Textarea)

class ContactsForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'mail', 'subject', 'content')