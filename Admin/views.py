# views.py en la app administrador
from django.shortcuts import render, redirect
from .forms import AdministradorRegistroForm, AdministradorLoginForm
from django.contrib import messages
from .models import Administrador

def registro_administrador(request):
    if request.method == 'POST':
        form = AdministradorRegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_administrador')
    else:
        form = AdministradorRegistroForm()
    return render(request, 'administrador/registro.html', {'form': form})

def login_administrador(request):
    if request.method == 'POST':
        form = AdministradorLoginForm(request.POST)
        if form.is_valid():
            matricula = form.cleaned_data['matricula']
            nombre_usuario = form.cleaned_data['nombre_usuario']
            try:
                admin = Administrador.objects.get(matricula=matricula, nombre_usuario=nombre_usuario)
                messages.success(request, f'Bienvenido administrador {admin.nombre}')
                # Redirigir al panel de administrador después del inicio de sesión
                return redirect('index2a')
            except Administrador.DoesNotExist:
                messages.error(request, 'Matrícula o contraseña incorrectos')
    else:
        form = AdministradorLoginForm()
    return render(request, 'administrador/login.html', {'form': form})

def logout(request):
    logout(request)
    messages.success(request, "Sesión cerrada exitosamente")
    return redirect('index')

