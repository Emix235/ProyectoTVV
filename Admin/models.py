from django.db import models

class Administrador(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    GENERO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    ]
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES)
    nombre_usuario = models.CharField(max_length=100)
    matricula = models.CharField(max_length=100)
    pais_origen = models.CharField(max_length=100)
    imagen_perfil = models.ImageField(upload_to='imagenes_perfil/', null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"
