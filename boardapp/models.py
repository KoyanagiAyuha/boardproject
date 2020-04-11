from django.db import models

# Create your models here.
class BoardModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=30)
    images = models.ImageField(upload_to='', null=True, blank=True)
    good = models.IntegerField(null=True, blank=True, default=0)
    read = models.IntegerField(null=True, blank=True, default=0)
    readuser = models.CharField(max_length=200, null=True, blank=True, default='')
