from django.urls import path
from . import views
app_name = 'contactus'
urlpatterns = [
    #path('', views.index, name='index'),
    #path('', views.ContactCreateView.as_view(), name="index"),
    path('', views.send_message, name="index"),
    path('contactus/<slug:pk>', views.ContactDetails.as_view(), name = 'contacts-us'),
]
