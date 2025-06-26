from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import AppointmentShare
from .serializers import AppointmentShareSerializer

@api_view(['GET', 'POST'])
def appointment_share_list(request):
    if request.method == 'GET':
        shares = AppointmentShare.objects.all()
        
        appointment_id = request.query_params.get('appointment', None)
        if appointment_id:
            shares = shares.filter(appointment_id=appointment_id)

        colaborator_id = request.query_params.get('shared_with', None)
        if colaborator_id:
            shares = shares.filter(shared_with=colaborator_id)
            
        serializer = AppointmentShareSerializer(shares, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AppointmentShareSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def appointment_share_detail(request, pk):
    try:
        share = AppointmentShare.objects.get(pk=pk)
    except AppointmentShare.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AppointmentShareSerializer(share)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AppointmentShareSerializer(share, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        share.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)