from django.contrib.auth.backends import BaseBackend
from .models import Usuario

class CustomAuthBackend(BaseBackend):
    def authenticate(self, request, nombreusuario=None, password=None):
        try:
            usuario = Usuario.objects.get(nombreusuario=nombreusuario)
            if usuario.check_password(password):
                return usuario
        except Usuario.DoesNotExist:
            return None
