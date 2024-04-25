from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.models import User
from usuario.models import Usuario
from games.models import Game
from games.forms import GameForm
from django.shortcuts import render, redirect, get_object_or_404
#from users.forms import UserProfileForm
#from users.models import
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from usuario.forms import PerfilForm
#from Compra.forms import CompraForm


def index(request):
    games = Game.objects.all()
    return render(request, 'index.html', {
        'games': games,
    })

def index2(request):
    games = Game.objects.all()
    users = Usuario.objects.all()
    return render(request, 'administrador/index.html', {'users': users, 'games': games, })


def index3(request):
    games = Game.objects.all()
    users = Usuario.objects.all()
    return render(request, 'usuario/index.html', {'users': users, 'games': games, })


'''
def login_view(request):
    games = Game.objects.all()
    if request.user.is_authenticated:
        return redirect('index2u')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "Bienvenido {}".format(user.username))
            return redirect('index2u')
        else:
            messages.error(request, "Usuario o contraseña no válidos")

    return render(request, 'users/login.html', {})


def logout_view(request):
    logout(request)
    messages.success(request, "Sesión cerrada exitosamente")
    return redirect('index')


def registrar(request):
    if request.user.is_authenticated:
        return redirect('index')
    form = RegisterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        # user = User.objects.create_user(username, email, password)
        user = form.save()
        if user:
            login(request, user)
            messages.success(request, "Usuario creado correctamente")
            return redirect('index')

    return render(request, 'users/newuser.html', {
        'form': form,
    })
'''

'''
def mostrar_usuario(request, user_id):
    usuario = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            # Redirigir a alguna página después de guardar los datos
            return HttpResponseRedirect('index3')
    else:
        form = UserProfileForm(instance=usuario)

    return render(request, 'users/perfil.html', {'usuario': usuario, 'form': form})
'''


'''
def login_view_admin(request):
    if request.user.is_authenticated:
        return redirect('index2a')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "Bienvenido administrador:  {}".format(user.username))
            return redirect('index2a')
        else:
            messages.error(request, "Usuario o contraseña no válidos")

    return render(request, 'administrator/login.html', {})


def logout_admin(request):
    logout(request)
    messages.success(request, "Sesión cerrada exitosamente")
    return redirect('index')


def registrar_admin(request):
    if request.user.is_authenticated:
        return redirect('index')
    form = RegisterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        # user = User.objects.create_user(username, email, password)
        user = form.save()
        if user:
            login(request, user)
            messages.success(request, "Usuario administrador creado correctamente")
            return redirect('index')

    return render(request, 'administrator/newadmin.html', {
        'form': form,
    })
'''

def agregar_juego(request):
    games = Game.objects.all()
    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirigir a la página de inicio después de agregar el juego
    else:
        form = GameForm()
    return render(request, 'administrador/agregar_juegos.html', {'form': form, 'games': games})


def edit_game(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES, instance=game)
        if form.is_valid():
            form.save()
            return redirect('index2a')
    else:
        form = GameForm(instance=game)
    return render(request, 'administrador/edit_game.html', {'form': form})


def delete_game(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    if request.method == 'POST':
        game.delete()
        return redirect('index2a')
    return render(request, 'administrador/delete_game.html', {'game': game})


'''
def realizar_pago(request):
    if request.method == 'POST':
        form = CompraForm(request.POST)
        if form.is_valid():
            form.save()  # Guardar la compra en la base de datos
            # Limpiar el carrito de compras
            # Redirigir a una página de confirmación de pago o a cualquier otra página
            return redirect('pagina_de_confirmacion')
    else:
        form = CompraForm()

    return render(request, 'users/comprar_juego.html', {'form': form})
'''