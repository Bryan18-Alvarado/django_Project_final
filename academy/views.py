from django.shortcuts import render


from .models import Courses,Blog, Documentation, Contact_us



from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm


from .forms import RegistrationForm
from .forms import CustomAuthenticationForm



def custom_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')  # Redirige al usuario después de un inicio de sesión exitoso
        # No necesita else aquí
    else:
        form = CustomAuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            if request.user.is_authenticated:
                return redirect('index')
              # Redirige a la página de inicio después del registro
    else:
        form = RegistrationForm()

    return render(request, 'registration/register.html', {'form': form})



def index(request):
        return render(request,'index.html')
    
def courses (request):
    courses = Courses.objects.all()
    return render(request, 'courses/courses.html', {'courses': courses})

    
def blog(request):
    blogs = Blog.objects.all()  
    return render(request, 'blog/blog.html', {'blogs':blogs})

def documentation(request):
    documentation = Documentation.objects.all()
    return render (request, 'documentation/documentation.html', {'documentations': documentation})
    
def contact_us(request):
    contact_us = Contact_us.objects.all()
    return render(request, 'contact_us/contact_us.html', {'contact_us': contact_us})
