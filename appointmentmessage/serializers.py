from rest_framework import serializers
from .models import AppointmentMessage

class AppointmentMessageSerializer(serializers.ModelSerializer):

    timestamp = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = AppointmentMessage
        fields = (
            'pk',
            'appointment',
            'user',
            'content',
            'timestamp',
        )