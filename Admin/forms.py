# forms.py en la app administrador
from django import forms
from .models import Administrador
from django.contrib.auth.forms import UserCreationForm


class AdministradorRegistroForm(forms.ModelForm):
    imagen_perfil = forms.ImageField(required=False)  # Campo de imagen de perfil

    class Meta:
        model = Administrador
        fields = ['nombre', 'apellidos', 'edad', 'genero', 'nombre_usuario', 'matricula', 'pais_origen',
                  'imagen_perfil']

class AdministradorLoginForm(forms.Form):
    nombre_usuario = forms.CharField(max_length=100)
    matricula = forms.CharField(max_length=100, widget=forms.PasswordInput)


class AdministradorForm(forms.ModelForm):
    class Meta:
        model = Administrador
        fields = ['nombre', 'apellidos', 'edad', 'genero', 'nombre_usuario', 'matricula', 'pais_origen',
                  'imagen_perfil']
