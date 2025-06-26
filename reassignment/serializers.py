from rest_framework import serializers
from reassignment.models import Reassignment
from staff.models import Staff
from appointment.models import Appoinment

class ReassignmentSerializer(serializers.ModelSerializer):
    appointment_title = serializers.CharField(source='appointment.titulo', read_only=True)
    
    requesting_worker_name = serializers.CharField(source='requesting_worker.name', read_only=True)


    class Meta:
        model = Reassignment
        fields = (
            'id', 
            'appointment',
            'appointment_title',
            'requesting_worker',
            'requesting_worker_name',
            'reason',
            'status',
            'requested_at',
            'updated_at',
        )
        read_only_fields = ('requested_at', 'updated_at', 'appointment_title', 'requesting_worker_name')

    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
