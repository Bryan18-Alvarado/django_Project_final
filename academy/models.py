from django.db import models


# Create your models here.

class Courses(models.Model):
    title = models.CharField(max_length=100)
    image= models.ImageField (upload_to="courses\image")
    url= models.URLField(blank=True)
    
    def  __str__(self):
        return self.title
    
class Blog(models.Model):
    title = models.CharField(max_length=100)
    image= models.ImageField (upload_to="blog\image")
    url= models.URLField(blank=True)
    
    def  __str__(self):
        return self.title
class Documentation(models.Model):
    title = models.CharField(max_length=100)
    image= models.ImageField (upload_to="documentation\image")
    url= models.URLField(blank=True)
    
    def  __str__(self):
        return self.title
class Contact_us(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image= models.ImageField (default='default_image.jpg')
    
    def  __str__(self):
        return self.title   