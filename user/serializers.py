from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework.exceptions import ValidationError

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  

    class Meta:
        model = get_user_model()
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
        )

    def validate_assigned_clients(self, value):
        for client in value:
            if client.role != 'client':
                raise serializers.ValidationError("Only users with role 'client' can be assigned.")
        return value

    def validate(self, data):
        role = data.get('role', getattr(self.instance, 'role', None))
        assigned_clients = data.get('assigned_clients', None)

        if role == 'client' and assigned_clients:
            raise serializers.ValidationError("A client cannot have assigned clients.")
        
        return data

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = get_user_model().objects.create(**validated_data)
        user.password = make_password(password)
        user.save()
        return user
