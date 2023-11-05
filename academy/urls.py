from django.urls import path
from . import views
from django.contrib  import admin

urlpatterns = [
    path('', views.index, name='index'),
    path('courses/', views.courses, name='courses'),
    path('blog/', views.blog, name='blog'),
    path('documentation/', views.documentation, name='documentation'),
    path('contact_us/', views.contact_us, name='contact_us'),
]