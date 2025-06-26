from rest_framework import serializers
from .models import Client 

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = (
            'id',
            'name',
            'email',
            'dni',
            'phone',
            'registration_date',
            'password',
            'photo',
        )
        read_only_fields = ('registration_date',)

    def update(self, instance, validated_data):
        if 'photo' in validated_data:
            if instance.photo and validated_data['photo'] != instance.photo:
                
                instance.photo.delete(save=False) 

        return super().update(instance, validated_data)

