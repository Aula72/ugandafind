from django.urls import path
from django.conf.urls import url
from . import views
#num = '' 
app_name = 'ourapp'
urlpatterns = [
    path('', views.index, name='home'),
    path('articles', views.IndexView.as_view(), name='index'),
    #path('article/<int:pk>/', views.DetailView.as_view(), name = 'details'),
    path('article/<int:pk>/', views.related_article, name = 'details'),
    #path('articles/add/', views.ArticleCreate.as_view(), name = "new_article"),
    # path('articles/add/', views.CreateArticle.as_view(), name = "new_article"),
    # path('articles/add/', views.new_article, name = "new_article"),
     path('articles/add/', views.create_article, name = "new_article"),
    path('articles/edit/<int:art_id>/', views.edit_article, name = "edit_article"),
    path('articles/type/<art_type>', views.some_articles, name = "some_articles"),
    path('articles/user/<art_user>/', views.user_articles, name = "my_articles"),
    #path('articles/edit/<string:id>/', views.edit_article, name = "edit_article"),
    path('articles/photo/', views.PhotoCreate.as_view() , name = "new_photo"),
    # path('register/', views.UserFormView.as_view(), name='register'),
    path('register/', views.signup, name='register'),
    path('search/', views.searches, name="search-results"),
    path('logout/', views.logout_view, name='logout'),
    #path('login/', views.login_view, name="logged-in")
    path('rats/', views.form_viewing, name="easy"),
    path('user/<int:ids>/', views.user_profile, name="my-profile"),
    path('your-message/', views.MessageFormView.as_view(), name="your-message"),
    #path('') 
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    path('reset-password/', views.remember_password, name="reset-password"),
]