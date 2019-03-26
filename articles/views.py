from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContentForm, ReferForm
#from django.views.generic import CreateView, UpdateView,DeleteView, DetailView
from django.views import generic
from .models import Content, Refer
from django import forms
from django.urls import reverse_lazy
# Create your views here.
def index(request):
    return HttpResponse('iu54tu but4iu4tu hut5i4')

class ContentCreate(generic.CreateView):
    # form = ContentForm
    # template = 'articles/create.html'
    model = Content
    
    fields = ['title', 'body', 'references']

class MutliForms(generic.FormView):
    template_name = 'articles/create.html'
    form_classes = {
        'content': ContentForm,
        'refer': ReferForm
    }
    success_urls = {
        'content' : reverse_lazy('keep_content'),
        'refer' : reverse_lazy('keep_refer')
    }
    def content_from_valid(self, form):
        pass
    def refer_form_valid(self, form):
        pass


class ContentView(generic.FormView):
    form_class =  ContentForm
    success_url = 'articles:new_article'
    template_name = 'articles/create.html'

    def dispatch(self,request, *args, **kwargs):
        return super(ContentView, self).dispatch(request, *args, **kwargs)
        #some thing here

    def get_context_data(self, **kwargs):
        context = super(Content, self).get_context_data(**kwargs)
        context['content_view_in_action'] = True
        return context

class ReferView(generic.FormView):
    form_class =  ReferForm
    success_url = 'articles:new_article'
    template_name = 'articles/create.html'

    def dispatch(self,request, *args, **kwargs):
        return super(ReferView, self).dispatch(request, *args, **kwargs)
        #some thing here

    def get_context_data(self, **kwargs):
        context = super(ReferView, self).get_context_data(**kwargs)
        context['content_view_in_action'] = False
        return context