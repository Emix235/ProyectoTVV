from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Usuario
from django import forms
from django.contrib.auth.models import User

'''
class UsuarioRegistroForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    imagen_perfil = forms.ImageField(required=False)  # Agregar campo de imagen
    class Meta:
        model = Usuario
        fields = ['nombreusuario', 'nombre', 'apellido', 'correo', 'fecha_nacimiento', 'password', 'imagen_perfil']  # Agregar campo de imagen
'''

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombreusuario', 'nombre', 'apellido', 'correo', 'fecha_nacimiento', 'password', 'imagen_perfil']
        widgets = {
            'password': forms.PasswordInput(),
        }

class UsuarioLoginForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombreusuario', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }


class PerfilForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'correo', 'fecha_nacimiento', 'imagen_perfil']  # Agregar campo de imagen
        widgets = {
            'imagen_perfil': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }