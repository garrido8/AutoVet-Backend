from rest_framework import serializers
from .models import Conversation 

class ConversationSerializer(serializers.ModelSerializer):
    
    client_name = serializers.CharField(source='client.name', read_only=True)

    class Meta:
        model = Conversation
        fields = (
            'id',
            'client',
            'client_name', 
            'title',
            'created_at',
        )
        read_only_fields = ('created_at', 'client_name') 
