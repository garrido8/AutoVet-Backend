from rest_framework import serializers
from .models import AppointmentShare
from staff.models import Staff

class AppointmentShareSerializer( serializers.ModelSerializer ):
    shared_with = serializers.PrimaryKeyRelatedField(
        queryset = Staff.objects.all( )
    )

    class Meta:
        model = AppointmentShare
        fields = [
            'id',
            'appointment',
            'shared_with', 
            'shared_by',   
            'permission',
            'shared_at',
        ]
        read_only_fields = [ 'shared_at' ]