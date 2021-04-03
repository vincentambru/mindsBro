from django.db import models

# Create your models here.
class blogPage(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=200,blank=False)

    def __str__(self):
        return self.title

class dynamicPage(models.Model):
    image = models.ImageField(upload_to='dynamic/', blank=False)
    logo = models.ImageField(upload_to='dynamic/', blank=False)
    name = models.CharField(max_length=50, blank=False)
    title = models.CharField(max_length=100, blank=False)
    date = models.CharField(max_length=50, blank=False)
    description = models.TextField(max_length=500,blank=False)

    def __str__(self):
        return self.title

class sliderPage(models.Model):
    image = models.ImageField(upload_to='slider/', blank=False)
    logo = models.ImageField(upload_to='slider/', blank=False)
    title = models.CharField(max_length=100, blank=False)