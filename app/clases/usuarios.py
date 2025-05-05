from django.db import models
from django.utils import timezone

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    dni = models.CharField(max_length=15, unique=True)
    fecha_nacimiento = models.DateField()
    fecha_creacion = models.DateTimeField(default=timezone.now)
    numero_billetera = models.CharField(max_length=50, unique=True)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.email})"
