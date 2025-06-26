from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.db.models import Q

from .models import Appoinment
from .serializers import AppoinmentSerializer

@api_view(['GET', 'POST'])
def appoinment_list(request):
    if request.method == 'GET':
        appoinments = Appoinment.objects.all()

        pet_id = request.query_params.get('mascota', None)
        if pet_id:
            appoinments = appoinments.filter(mascota_id=pet_id)

        trabajador_asignado_param = request.query_params.get('trabajador_asignado', None)
        if trabajador_asignado_param == 'null':
            appoinments = appoinments.filter(trabajador_asignado__isnull=True)
        elif trabajador_asignado_param:
            appoinments = appoinments.filter(trabajador_asignado_id=trabajador_asignado_param)

        serializer = AppoinmentSerializer(appoinments, context={'request': request}, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AppoinmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def appoinment_detail(request, pk):
    try:
        appoinment = Appoinment.objects.get(pk=pk)
    except Appoinment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AppoinmentSerializer(appoinment, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AppoinmentSerializer(appoinment, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        appoinment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)