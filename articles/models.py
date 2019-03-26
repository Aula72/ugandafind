from django.db import models
from django.conf import settings
import datetime
from ckeditor.fields import RichTextField
class Content(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length = 250)
    #body = models.TextField()
    body = RichTextField()
    photo = models.FileField(null=True)
    references = models.TextField(default='r8yu8 8ure4r8')
    date_create = models.DateTimeField('Date Created', default=datetime.datetime.now())
    date_update = models.DateTimeField('Date Update',  default=datetime.datetime.now())

class Refer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    reference = models.CharField(max_length = 800)
    date_created = models.DateTimeField()
    date_updated  = models.DateTimeField()

