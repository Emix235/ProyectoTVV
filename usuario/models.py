from django.db import models
from django.core.validators import FileExtensionValidator

class Usuario(models.Model):
    nombreusuario = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    fecha_nacimiento = models.DateField()
    password = models.CharField(max_length=120)
    imagen_perfil = models.ImageField(upload_to='imagenes_perfil/', null=True, blank=True, validators=[FileExtensionValidator(['jpg', 'jpeg', 'png'])])  # Agregar campo de imagen
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"<User: {self.id} {self.nombre} {self.apellido} {self.correo} {self.imagen_perfil}>"


