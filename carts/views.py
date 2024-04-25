from django.shortcuts import render, redirect, get_object_or_404

from .models import Cart
from .utils import get_or_create_cart
from games.models import Game
from .models import CartGames
from usuario.models import Usuario


def cart(request):
    cart = get_or_create_cart(request)
    usuario_id = request.session.get('usuario_id')
    usuario = None

    if usuario_id:
        usuario = get_object_or_404(Usuario, pk=usuario_id)
        # Asignar el usuario al carrito si está autenticado
        cart.user = usuario
        cart.save()

    return render(request, 'carts/cart.html', {
        'cart': cart,
        'usuario_autenticado': usuario is not None,
        'usuario': usuario,
    })


'''
def cart(request):
    usuario_id = request.session.get('usuario_id')
    if usuario_id:
        cart, created = Cart.objects.get_or_create(user_id=usuario_id)
    else:
        cart = None

    usuario = None
    if usuario_id:
        usuario = Usuario.objects.get(pk=usuario_id)

    return render(request, 'carts/cart.html', {
        'cart': cart,
        'usuario_autenticado': usuario_id is not None,
        'usuario': usuario,
    })
'''


'''
def add(request):
    usuario_id = request.session.get('usuario_id')
    if usuario_id:
        cart = get_or_create_cart(request)
        game = get_object_or_404(Game, pk=request.POST.get('game_id'))
        # quantity = int(request.POST.get('quantity', 1))
        cart_games = CartGames.objects.create_or_update_quantity(
            cart=cart,
            game=game,
            #    quantity=quantity
        )
        usuario = Usuario.objects.get(pk=usuario_id)
        return render(request, 'carts/add.html', {
            'game': game,
            'usuario_autenticado': True,
            'usuario': usuario,
        })
    else:
        # Si el usuario no está autenticado, redirigir al login
        return redirect('login_usuario')
'''

def add(request):
    usuario_id = request.session.get('usuario_id')
    if usuario_id:
        cart = get_or_create_cart(request)
        game = get_object_or_404(Game, pk=request.POST.get('game_id'))
        cart_games = CartGames.objects.create_or_update_quantity(
            cart=cart,
            game=game,
        )
        usuario = Usuario.objects.get(pk=usuario_id)
        return render(request, 'carts/add.html', {
            'game': game,
            'usuario_autenticado': True,
            'usuario': usuario,
        })
    else:
        # Si el usuario no está autenticado, redirigir al login
        return redirect('login_usuario')


def remove(request):
    cart = get_or_create_cart(request)
    game = get_object_or_404(Game, pk=request.POST.get('game_id'))

    cart.games.remove(game)

    return redirect('carts:cart')
