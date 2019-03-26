from django.db import models
#from django.core.urlresolvers import reverse 
from django.urls import reverse
from django.conf import settings
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
import datetime
from django.utils import timezone
from time import timezone
USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')
def get_user():
    #user = USER_MODEL
    pass
class Article(models.Model):
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
    # user = models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE)
    # user = models.ForeignKeyUser,to_field='id', default='',null=True, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article_title = models.CharField(max_length=400)
    article_body = RichTextUploadingField(blank=True, null=True)
    article_type = models.CharField(max_length=1, choices=ARTICLE, null=True, blank=True)
    article_references  = models.CharField(max_length=1000, null=True, blank=True)
    # article_created = models.DateTimeField(auto_now_add=True, null=True,blank=True)
    # article_updated = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    def get_absolute_url(self):
        return reverse('ourapp:details', kwargs={'pk':self.pk})
    def __str__(self):
        if self.article_type is not None:
            return self.article_title+'-----'+self.article_type
        else:
            return self.article_title


class Reference(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,to_field='id', on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    reference_text = models.CharField(max_length=9000)
    def __str__(self):
        return self.reference_text

class Photo(models.Model):
    user = models.ForeignKey(USER_MODEL,to_field='id', on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    description = models.CharField(max_length= 1000)
    image = models.FileField(default=None)
    #photo = models.FileField()
    def __str__(self):
        return self.description

class Message(models.Model):
    name = models.CharField(max_length=500)
    email = models.EmailField()
    message = models.TextField()


#filtering data
#Article.objects.all() #all the articles
#Article.objects.filter(id=5) #where id =5
#Artictle.objects.filter(article_title__startswith='i am happy')#begigs with am happy
#.......................(article_title__endswith="happy")
#.......................(article_title__contains="happy")