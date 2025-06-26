from rest_framework import serializers
from .models import Pet, Client  

class PetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pet
        fields = (
            'pk', 'propietario', 'nombre', 'especie', 'raza', 'edad',
            'sexo', 'peso', 'vacunado', 'esterilizado'
        )