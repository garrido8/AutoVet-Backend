from rest_framework import serializers
from .models import Appoinment

class AppoinmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appoinment
        fields = (
            'pk',
            'mascota',
            'titulo',
            'descripcion',
            'fecha_creacion',
            'fecha_resolucion',
            'estado',
            'urgencia',
            'archivo_adjuntado',
            'trabajador_asignado',
        )
