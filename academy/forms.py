# En forms.py de tu aplicación
from django import forms
from django.contrib.auth.models import User

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from django.contrib.auth.forms import AuthenticationForm

class CustomAuthenticationForm(AuthenticationForm):
    error_messages = {
        'invalid_login': 'Nombre de usuario o contraseña incorrectos. Por favor, inténtalo de nuevo.',
    }


class RegistrationForm(UserCreationForm):
    username = forms.CharField(
        label="Nombre de usuario",
        max_length=150,
    )

    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput,
    )

    password2 = forms.CharField(
        label="Confirmar contraseña",
        widget=forms.PasswordInput,
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

