"""
URL configuration for ProyectoTVV project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from games.views import GameListView
from games.views import GameListView2_u, agregar_juego


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', GameListView.as_view(), name='index'),

    path('usuarios/index', GameListView2_u.as_view(), name='index2u'),
    #path('usuarios/index', views.index3, name='index2u'),
    path('administrador/index', views.index2, name='index2a'),

    #path('administrador/agregar-juego', views.agregar, name='agregar'),

    path('administrador/agregar', views.agregar_juego, name='agregar_juego'),
    path('editar/<int:game_id>/', views.edit_game, name='editar_juego'),
    path('eliminar/<int:game_id>/', views.delete_game, name='eliminar_juego'),

    #path('usuarios/<int:user_id>/', views.mostrar_usuario, name='mostrar-usuario'),

    #path('usuarios/login', views.login_view, name='login'),
    #path('administrador/login', views.login_view_admin, name='login_admin'),

    #path('usuarios/logout', views.logout_view, name='logout'),
    #path('administrador/logout', views.logout_admin, name='logout_admin'),
    #path('usuarios/registro', views.registrar, name='registro'),
    #path('administrador/registro', views.registrar_admin, name='registro_admin'),
    path('juegos/', include('games.urls')),
    path('carrito/', include('carts.urls')),
    path('usuarios/', include('usuario.urls')),
    path('administrador/', include('Admin.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
