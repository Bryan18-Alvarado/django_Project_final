from django.shortcuts import render

# Create your views here.
from .models import Courses,Blog, Documentation, Contact_us

def index(request):
        return render(request,'index.html')
    
def courses (request):
    courses = Courses.objects.all()
    return render(request, 'courses/courses.html', {'courses': courses})

    
def blog(request):
    blogs = Blog.objects.all()  
    return render(request, 'blog/blog.html', {'blogs':blogs})

def documentation(request):
    documentations = Documentation.objects.all()
    return render (request, 'documentation/documentation.html', {'documentations': documentation})

def contact_us(request):
    contact_us = Contact_us.objects.all()
    return render(request, 'contact_us/contact_us.html', {'contact_us': contact_us})
    