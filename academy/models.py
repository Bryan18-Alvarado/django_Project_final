from django.db import models


# Create your models here.
class Courses(models.Model):
    title = models.CharField(max_length=100)
    description=models.CharField(max_length=250)
    image= models.ImageField (upload_to="courses\image")
    url= models.URLField(blank=True)
    
class Blog(models.Model):
    title = models.CharField(max_length=100)
    description=models.CharField(max_length=250)
    image= models.ImageField (upload_to="blog\image")
    url= models.URLField(blank=True)
    
class Documentation(models.Model):
    title = models.CharField(max_length=100)
    description=models.CharField(max_length=250)
    image= models.ImageField (upload_to="documentation\image")
    url= models.URLField(blank=True)
    
class Contact_us(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    url= models.URLField(blank=True)