# urls.py en la app administrador
from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registro_administrador, name='registro_administrador'),
    path('login/', views.login_administrador, name='login_administrador'),
    path('logout/', views.logout, name='logout_administrador'),

    # Agrega otras URLs según sea necesario
]
