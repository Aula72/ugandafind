from django.views import generic
from .models import Article, Photo, Message
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
import operator
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, HttpResponse
#registration and login 
# from  django.contrib.auth.models.User import 
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from .forms import UserForm, LoginForm, NewArticleForm, MessageForm,ArticleForm
import datetime
import random

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage

# users = User.objects.get(pk=request.user.id)
def index(request):    
    return render(request, 'ourapp/home.html')
class IndexView(generic.ListView):
    template_name="ourapp/index.html"
    context_object_name = 'all_article' #default is 'object_list' here its overriden
    def get_queryset(self):
        return Article.objects.all().order_by('-id')[:10]
class DetailView(generic.DetailView):
    model = Article
    template_name = "ourapp/articles/show.html"  
          

class ArticleCreate(CreateView):
    model = Article    
    fields = ['article_title', 'article_type','article_body', 'article_references']

class ArticleUpdate(UpdateView):
    model = Article
    fields = ['article_title', 'article_body', 'article_reference'] 

class ArticleDelete(DeleteView):
    model = Article
    success_url = reverse_lazy('index')

class PhotoCreate(CreateView):
    model = Photo
    fields = ['image']

class UserFormView(View):
    form_class = UserForm
    template_name = 'ourapp/registration.html'

    #display blank form for new user
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    #submit for registration
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():            
            user = form.save(commit=False)
            email =  form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # confirm_password = form.confirm_password['confirm_password']
            user.set_password(password) 
            # if password==confirm_password:          
            user.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('ourapp:index')
            else:
                pass
        #else register
        return render(request, self.template_name, {'form':form})

def login_view(request):
    form = LoginForm(request.POST or None)
    next = request.GET.get('next')
    if form.is_valid():
        username = form.cleaned_data('username')
        password = form.cleaned_data('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect("/")
    return render(request, "ourapp/login.html", {"form":form})
def logout_view(request):
    logout(request)
    return redirect('ourapp:index')

#search site
def searches(request): 
    not_allowed = ['is', 'a', 'the', 'our', 'it', 'must', 'them', 'oh', '']   
    query = request.GET.get('q')
    if query:
        articles =  Article.objects.filter(Q(article_title__icontains=query)| 
                    Q(article_body__icontains=query) | 
                    Q(article_references__icontains=query)) 
        paginate = Paginator(articles, 2)
        page = request.GET.get('page')
        articles = paginate.get_page(page)  
        t=render(request, 'ourapp/search.html', {'articles':articles, 'q':query})

    else:         
        t=render(request, 'ourapp/search.html',{'q':query})      
    return t


#@login_required(login_url="login/")
# def new_article(request):      
#     next = request.GET.get('next')
#     if request.method=='POST':
#         instance = Article(request.user.username)
#         form = ArticleForm(request.POST, instance=instance)        
#         print(form.errors)
#         if form.is_valid():
#             Article.objects.create(**form.cleaned_data) 
#             return redirect('ourapp:index')
            
#     else:
#         pass
#     return render(request, 'ourapp/ourform.html')#, {'form':form})
#@login_required(login_url="login/")
def edit_article(request, art_id=None):
    next = request.GET.get('next')
    try:
        article = get_object_or_404(Article, id=art_id) 
        if request.method=='POST':
            form = NewArticleForm(request.POST or None,request.FILES, 
                initial={"article_body":article.article_body, "article_references":article.article_references,
                "article_type":article.article_type, "article_title":article.article_title
            })
            if form.is_valid():
                articles = form.save(commit=False)
                articles.user = request.user
                articles.save()
                return redirect('ourapp:index')
        return render(request, 'ourapp/articles/update.html', {'form':form})
    except Article.DoesNotExist:
        info = 'The Article Does Not Exist'
        return render(request, 'ourapp/not_exist.html', {'info':info})
    

#some articles#
def some_articles(request, art_type):
    art =results = ' '
    if  art_type =='political history':
        art = 'P'
    elif art_type=='agriculture':
        art = 'A'
    elif art_type=='education':
        art = 'E'
    elif art_type=='economics':
        art = 'I'
    elif art_type=='culture':
        art = 'C'
    elif art_type=='religion':
        art = 'R'
    elif art_type=='sports and games':
        art = 'S'
    elif art_type=='tourism':
        art = 'T'
    elif art_type=='geography':
        art = 'G'
    else:
        art = 'H'
    
    articles = Article.objects.filter(article_type=str(art))
    articles = paginating(request, articles)
    return render(request, 'ourapp/some_articles.html', {'articles':articles, 'art_type':art_type})
def user_articles(request, art_user=None):
    art_user = request.user.id
    articles = Article.objects.filter(user=str(art_user))
    articles = paginating(request, articles)
    return render(request, 'ourapp/my_articles.html', {'articles':articles})


class CreateArticle(View):
    user = "1";
    form_class = ArticleForm(initial={"user":user})  
    template_name = 'ourapp/new_article.html'

    def get(self,request):
        form = self.form_class
        return render(request, self.template_name, {'form':form})  
    
    def post(self, request):
        if request.method=='POST':# and form.is_valid():            
            print('iujfoeirfe ')
            form = ArticleForm(request.POST)
            # form.user.initial(request.user)
            print(form.errors)
            if form.is_valid():
                print(form.is_valid())
                return redirect('/articles/user/'+str(request.user.id)+'/')

        return render(request, self.template_name, {'form':form})
    
def related_article(request,  pk):
    try:
        articles = Article.objects.filter(id=pk)
        # articles = get_object_or_404(Article, pk=pk)
        for i in articles:
            x = i.article_type
        new_art = Article.objects.filter(article_type=x)[5:]   
        return render(request, 'ourapp/articles/show.html', {'new_art':new_art, 'articles':articles})
    except UnboundLocalError:
        return render(request, '404.html', {})

def new_article(request):
    # ref = User
    # userid = request.user
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    if not request.user.is_authenticated:
        raise Http404
    form = ArticleForm(request.POST or None, request.FILES or None)
    # print(User.pk)
    if form.is_valid():
        article = form.save(commit=False)
        article.user = request.user.id
        # article.user = ref.natural_key(request.user)
        # print(User.pk)
        # print(article.user)
        article.save()
        return redirect('/index/')
    else:
        print(form.errors)
        # print(ref.natural_key(request.user))
    return render(request, 'ourapp/new_article.html', {'form':form})

def form_viewing(request):
    form = NewArticleForm()
    if  request.method=='POST':
        form = NewArticleForm(request.POST)
        if form.is_valid():
            Article.User = request.user
            Article.objects.create(**form.cleaned_data) 
            print(form.cleaned_data)
        else:
            print(form.errors())
    return render(request, 'ourapp/rats.html', {'form':form})


class MessageFormView(View):
    form_class = MessageForm
    template_name = 'ourapp/message.html'
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid(): 
            Message.objects.create(**form.cleaned_data)
            
        return render(request, self.template_name, {'form':form})

def paginating(request, list_of_items):
    paginate = Paginator(list_of_items, 10)
    page = request.GET.get('page')
    list_of_items = paginate.get_page(page)
    return list_of_items

def error_404(request):
    data = {}
    return render(request,'ourapp/error_404.html', data)

def error_500(request):
    data = {}
    return render(request,'ourapp/error_500.html', data)

# @login_required(login_url="login/")
def create_article(request):
    # require_login(request)
    if request.method=="POST":
        form = ArticleForm(request.POST, request.FILES) 
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('ourapp:index') 
    else:
        form = ArticleForm()
    
    return render(request, 'ourapp/new_article.html', {"form":form})


def user_profile(request, ids):
    user = User.objects.get(pk=ids)
    articles = Article.objects.filter(user=ids).count()
    return render(request, 'ourapp/user.html', {'user':user, "articles":articles})

def require_login(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/?next=%s'%request.path)

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('ourapp/acc_account.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return render(request, 'ourapp/confirm.html', {'to_email':to_email})
    else:
        form = UserForm()
    return render(request, 'ourapp/registration.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')

def remember_password(request):
    return render(request, 'ourapp/remember_password.html')