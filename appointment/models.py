from django.db import models
from pet.models import Pet
from staff.models import Staff

class Appoinment(models.Model):
    mascota = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='incidencias')
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_resolucion = models.DateTimeField(null=True, blank=True)
    estado = models.CharField(
        max_length=20,
        choices=(
            ('pendiente', 'Pendiente'),
            ('en_proceso', 'En proceso'),
            ('resuelta', 'Resuelta'),
            ('esperando', 'Esperando cliente'),
        ),
        default='pendiente'
    )
    urgencia = models.BooleanField(default=False)
    archivo_adjuntado = models.FileField(upload_to='documentos_incidencias/', null=True, blank=True)

    trabajador_asignado = models.ForeignKey(
        Staff,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='incidencias_asignadas'
    )

    def __str__(self):
        return f"{self.titulo} ({self.estado})"
