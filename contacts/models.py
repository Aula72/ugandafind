from django.db import models
from django.urls import reverse, reverse_lazy, resolve
from django.utils import timezone
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length =100)
    mail = models.EmailField()
    subject = models.CharField(max_length = 250)
    content = models.TextField()
    created_at = models.DateField(default=timezone.now())
    def get_absolute_url(self):
        return reverse('details', kwargs={'pk':pk})
    def __str__(self):
        return self.name+'---'+self.mail