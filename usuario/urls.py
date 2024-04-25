# urls.py en la app usuario
from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registro_usuario, name='registro_usuario'),
    path('login/', views.login_usuario, name='login_usuario'),
    path('logout/', views.logout, name='logout_usuario'),
    path('perfil/', views.editar_perfil, name='editar_perfil'),
    # Agrega otras URLs según sea necesario
]
