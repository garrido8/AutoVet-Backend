from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.db.models import Q
from .models import AppointmentMessage
from .serializers import AppointmentMessageSerializer


@api_view(['GET', 'POST'])
def appointment_message_list(request):
    if request.method == 'GET':
        messages = AppointmentMessage.objects.all()

        appointment_id = request.query_params.get('appointment', None)
        if appointment_id:
            messages = messages.filter(appointment_id=appointment_id)

        serializer = AppointmentMessageSerializer(messages, context={'request': request}, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AppointmentMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def appointment_message_detail(request, pk):
    try:
        message = AppointmentMessage.objects.get(pk=pk)
    except AppointmentMessage.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AppointmentMessageSerializer(message, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AppointmentMessageSerializer(message, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        message.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)