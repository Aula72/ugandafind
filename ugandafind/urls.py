
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import include, handler404, handler500
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView
#from ourapp import views as my_views
#from django.contrib.auth import views as login_view
urlpatterns = [
    path('xednial/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    # url(r'^ckeditor/', include('ckeditor.urls')),
    path('select2/', include('django_select2.urls')),
    path('', include('ourapp.urls', namespace="OurApp")), #root urls
    path('ugandafind/contact-us/', include('contacts.urls', namespace="Contacts")),
    path('ugandafind/articles/', include('articles.urls', namespace="Article")),
    path('ugandafind/about-us/', include('aboutus.urls', namespace="About")),
    path('accounts/', include('django.contrib.auth.urls')), # new
    path('login/', LoginView.as_view(), name ='login'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# handler404 = my_views.error_404
# handler500 = my_views.error_500
#before hosting the app
# if settings:
#     urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
