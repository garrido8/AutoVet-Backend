from rest_framework import serializers
from .models import Staff
from client_user.models import Client 

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = (
            'pk',
            'name',
            'email',
            'dni',
            'phone',
            'registration_date',
            'role',
            'assigned_clients',
            'password',
            'photo',
        )
        read_only_fields = ('registration_date',)

    def validate_assigned_clients(self, value):
        for client in value:
            if not isinstance(client, Client):
                raise serializers.ValidationError("Only instances of Client can be assigned.")
        return value

    def update(self, instance, validated_data):
        if 'photo' in validated_data:
            if instance.photo and validated_data['photo'] != instance.photo:
                instance.photo.delete(save=False) 

        return super().update(instance, validated_data)

