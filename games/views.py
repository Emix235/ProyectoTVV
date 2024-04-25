# from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Game
from django.db.models import Q
from django.shortcuts import render, redirect
from .forms import GameForm
from usuario.models import Usuario


# Create your views here.

class GameListView(ListView):
    template_name = 'index.html'
    model = Game


'''
class GameListView2_u(ListView):
    template_name = 'usuario/index.html'
    model = Game

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario_id = self.request.session.get('usuario_id')
        if usuario_id:
            usuario = Usuario.objects.get(pk=usuario_id)
            context['usuario'] = usuario
            context['usuario_autenticado'] = True
        else:
            context['usuario_autenticado'] = False
        return context
'''


class GameListView2_u(ListView):
    template_name = 'usuario/index.html'
    model = Game

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario_id = self.request.session.get('usuario_id')
        usuario = None
        if usuario_id:
            try:
                usuario = Usuario.objects.get(pk=usuario_id)
            except Usuario.DoesNotExist:
                pass
        context['usuario'] = usuario
        context['usuario_autenticado'] = usuario is not None
        return context


class GameDetailView(DetailView):
    model = Game
    template_name = 'games/game.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        usuario_id = self.request.session.get('usuario_id')
        if usuario_id:
            usuario = Usuario.objects.get(pk=usuario_id)
            context['usuario'] = usuario
            context['usuario_autenticado'] = True
        else:
            context['usuario_autenticado'] = False
        return context


class GameDetailView2(DetailView):
    model = Game
    template_name = 'usuario/games/game.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        usuario_id = self.request.session.get('usuario_id')
        if usuario_id:
            usuario = Usuario.objects.get(pk=usuario_id)
            context['usuario'] = usuario
            context['usuario_autenticado'] = True
        else:
            context['usuario_autenticado'] = False
        return context


class GameSearchListView(ListView):
    template_name = 'games/search.html'
    model = Game.objects.all()

    def get_queryset(self):
        query = self.request.GET.get('q')

        object_list = Game.objects.filter(
            Q(nombre__icontains=query) | Q(precio__icontains=query) | Q(categoria__icontains=query)
        )
        return object_list


def agregar_juego(request):
    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirigir a la página de inicio después de agregar el juego
    else:
        form = GameForm()
    return render(request, 'agregar_juegos.html', {'form': form})
