from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Conversation
from .models import Client

from .serializers import ConversationSerializer 

@api_view(['GET', 'POST'])
def conversation_list(request):
    if request.method == 'GET':
        conversations = Conversation.objects.all()
        client_id = request.query_params.get('client_id', None)
        if client_id:
            try:
                client = Client.objects.get(pk=client_id)
                conversations = conversations.filter(client=client)
            except Client.DoesNotExist:
                return Response({"detail": "Client not found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ConversationSerializer(conversations, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        client_id = request.data.get('client')
        if not client_id:
            return Response({"client": "This field is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            client_instance = Client.objects.get(pk=client_id)
        except Client.DoesNotExist:
            return Response({"client": "Invalid client ID."}, status=status.HTTP_400_BAD_REQUEST)

        mutable_data = request.data.copy()
        mutable_data['client'] = client_instance.id

        serializer = ConversationSerializer(data=mutable_data)
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def conversation_detail(request, pk):
    conversation = get_object_or_404(Conversation, pk=pk)

    if request.method == 'GET':
        serializer = ConversationSerializer(conversation)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ConversationSerializer(conversation, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        conversation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
