from django.urls import path
from .views import GameDetailView, GameSearchListView, agregar_juego, GameDetailView2

app_name='juego'

urlpatterns = [

    path('search', GameSearchListView.as_view(), name='search'),
    path('<slug:slug>', GameDetailView.as_view(), name='juego'),
    path('usuarios/<slug:slug>', GameDetailView2.as_view(), name='juego2'),
]