# views.py en la app usuario
from .forms import RegistroForm, UsuarioLoginForm
from .forms import PerfilForm
from django.contrib import messages
from .forms import UsuarioLoginForm
from .models import Usuario
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import logout as django_logout
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django import template

register = template.Library()


def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login_usuario')
    else:
        form = RegistroForm()
    return render(request, 'usuario/registro.html', {'form': form})

'''
def login_usuario(request):
    if request.method == 'POST':
        form = UsuarioLoginForm(request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data['nombreusuario']
            contraseña = form.cleaned_data['password']
            try:
                usuario = Usuario.objects.get(password=contraseña, nombreusuario=nombre_usuario)
                request.session['usuario_id'] = usuario.id  # Almacenar solo el ID del usuario
                messages.success(request, f'Bienvenido: {usuario.nombreusuario}')
                return redirect('index2u')
            except Usuario.DoesNotExist:
                messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
    else:
        form = UsuarioLoginForm()
    return render(request, 'usuario/login.html', {'form': form})
'''


def login_usuario(request):
    if request.method == 'POST':
        form = UsuarioLoginForm(request.POST)
        if form.is_valid():
            nombreusuario = form.cleaned_data['nombreusuario']
            password = form.cleaned_data['password']
            try:
                usuario = Usuario.objects.get(nombreusuario=nombreusuario)
                if usuario.password == password:  # Verifica la contraseña
                    request.session['usuario_id'] = usuario.id  # Establece la sesión del usuario
                    return redirect('index2u')  # Redirigir a la página del perfil del usuario
                else:
                    # Manejar contraseña incorrecta
                    return render(request, 'usuario/login.html', {'form': form, 'error': 'Contraseña incorrecta'})
            except Usuario.DoesNotExist:
                # Manejar usuario no encontrado
                return render(request, 'usuario/login.html', {'form': form, 'error': 'Usuario no encontrado'})
    else:
        form = UsuarioLoginForm()
    return render(request, 'usuario/login.html', {'form': form})

'''
def login_usuario(request):
    if request.method == 'POST':
        form = UsuarioLoginForm(request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data['nombreusuario']
            contraseña = form.cleaned_data['password']
            try:
                usuario = Usuario.objects.get(password=contraseña, nombreusuario=nombre_usuario)
                request.session['usuario_id'] = usuario.id  # Almacenar solo el ID del usuario
                messages.success(request, f'Bienvenido: {usuario.nombreusuario}')
                return redirect('index2u')
            except Usuario.DoesNotExist:
                messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
    else:
        form = UsuarioLoginForm()
    return render(request, 'usuario/login.html', {'form': form})
'''



'''
def logout(request):
    django_logout(request)
    messages.info(request, "Has cerrado sesión correctamente.")
    return redirect('login_usuario')
'''

def logout(request):
    if 'usuario_id' in request.session:
        # Eliminar la clave 'usuario_id' de la sesión
        del request.session['usuario_id']
        # Establecer usuario_autenticado en False
        usuario_autenticado = False
        messages.success(request, "Sesión cerrada exitosamente")
    else:
        # Si la clave 'usuario_id' no está en la sesión, el usuario ya está cerrado
        messages.info(request, "El usuario ya está cerrado")
    return redirect('index')


'''
def editar_perfil(request):
    usuario_id = request.session.get('usuario_id')
    usuario_autenticado = usuario_id is not None

    try:
        usuario = Usuario.objects.get(pk=usuario_id)
    except Usuario.DoesNotExist:
        # Si el usuario no está autenticado, redirigir al login
        return redirect('login_usuario')

    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=usuario)
        if form.is_valid():
            form.save()
            # Mensaje de éxito
            messages.success(request, '¡Perfil actualizado correctamente!')
            return redirect('editar_perfil')
        else:
            # Mensajes de error si el formulario es inválido
            messages.error(request, 'Por favor, corrige los errores.')
    else:
        form = PerfilForm(instance=usuario)

    return render(request, 'usuario/perfil.html', {'form': form, 'usuario': usuario, 'usuario_autenticado': usuario_autenticado})
'''

def editar_perfil(request):
    usuario_id = request.session.get('usuario_id')
    usuario_autenticado = usuario_id is not None

    try:
        usuario = Usuario.objects.get(pk=usuario_id)
    except Usuario.DoesNotExist:
        # Si el usuario no está autenticado, redirigir al login
        return redirect('login_usuario')

    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=usuario)
        if form.is_valid():
            form.save()
            # Mensaje de éxito
            messages.success(request, '¡Perfil actualizado correctamente!')
            return redirect('editar_perfil')
        else:
            # Mensajes de error si el formulario es inválido
            messages.error(request, 'Por favor, corrige los errores.')
    else:
        form = PerfilForm(instance=usuario)

    return render(request, 'usuario/perfil.html', {'form': form, 'usuario': usuario, 'usuario_autenticado': usuario_autenticado})




