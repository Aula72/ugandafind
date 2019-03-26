from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import HiddenInput, TextInput, ChoiceWidget
from ckeditor.fields import RichTextFormField
from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from ckeditor.widgets import CKEditorWidget
from .models import Article, Message
class UserForm(UserCreationForm):
    # password = forms.CharField(widget = forms.PasswordInput)
    # confirm_password = forms.CharField(widget = forms.PasswordInput)
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    # def clean(self):
    #     cleaned_data=super(UserForm,self).clean
    #     password = cleaned_data.get("password")
    #     confirm_password = cleaned_data.get('confirm_password')
    #     if password != confirm_password:
    #         raise forms.ValidationError(
    #             "password and confirm_password does not match"
    #         )
        # if password != confirm_password:
        #     self.add_error('confirm_password', "Passwords don't match!")
        # return cleaned_data
class ArticleForm(forms.ModelForm):  
    # user = forms.MultipleChoiceField()
    # def __init__(self, *args, **kwargs):
    #     super(ArticleForm, self).__init__(*args, **kwargs)
    #     # self.fields['user'].queryset = Article.objects.filter(owner=self.request.user.id)  
    #     user = forms.ModelChoiceField(queryset=Article.objects.filter(user=request.user))
    # user = forms.IntegerField(widget=HiddenInput,required=True)
    # article_body = forms.CharField(widget = forms.Textarea(attr={'class':'richtexteditor'}))
    # article_references = forms.CharField(widget=TextInput({'class':'form-control', 'placeholder':'Add references separated by &&',\
    # }), required=True) 
    article_body = forms.CharField(widget=CKEditorWidget)
    class Meta:
        model = Article
        fields = ['article_title','article_type', 'article_body', 'article_references'] 

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username' , 'password']

class NewArticleForm(forms.Form):    
    ARTICLE =  (        
        ('P','political history'),
        ('H', 'healthy'),
        ('C', 'culture'),
        ('E', 'education'),
        ('R', 'religion'),
        ('I', 'economics'),
        ('A', 'agriculture'),
        ('S', 'sports and games'),
        ('G', 'geography'),
        ('T', 'tourism')
    )
    
    article_title = forms.CharField()
    article_type = forms.ChoiceField(choices=ARTICLE)
    article_body = forms.CharField(widget=CKEditorUploadingWidget())
    article_references = forms.CharField()
    
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'message']


         
    
    