from django.db import models
from client_user.models import Client

class Pet(models.Model):
    propietario = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='mascotas')
    nombre = models.CharField(max_length=50)
    especie = models.CharField(max_length=30)
    raza = models.CharField(max_length=50, blank=True)
    edad = models.IntegerField(null=True, blank=True)
    sexo = models.CharField(max_length=10, choices=(('macho', 'Macho'), ('hembra', 'Hembra')))
    peso = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    vacunado = models.BooleanField(default=False)
    esterilizado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nombre} ({self.especie})"