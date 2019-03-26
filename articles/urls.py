from django.urls import path
from . import views
app_name = "articles"
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.ContentCreate.as_view(), name='create_article'),
    path('new-article/', views.ContentView.as_view(), name = 'new_article'),
    path('new-reference/', views.ReferView.as_view(), name = 'new_article')
]
