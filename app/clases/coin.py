from django.db import models

class Coin(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    precio = models.DecimalField(max_digits=20, decimal_places=8)

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"
