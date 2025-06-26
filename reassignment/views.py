from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404 
from reassignment.models import Reassignment
from appointment.models import Appoinment
from staff.models import Staff

from .serializers import ReassignmentSerializer

@api_view(['GET', 'POST'])
def reassignment_list(request):
    if request.method == 'GET':
        reassignments = Reassignment.objects.all()

        appointment_id = request.query_params.get('appointment_id', None)
        requesting_worker_id = request.query_params.get('requesting_worker_id', None)
        status_filter = request.query_params.get('status', None)

        if appointment_id:
            try:
                appointment = Appoinment.objects.get(pk=appointment_id)
                reassignments = reassignments.filter(appointment=appointment)
            except Appoinment.DoesNotExist:
                return Response({"detail": "Appointment not found."}, status=status.HTTP_404_NOT_FOUND)
        
        if requesting_worker_id:
            try:
                requesting_worker = Staff.objects.get(pk=requesting_worker_id)
                reassignments = reassignments.filter(requesting_worker=requesting_worker)
            except Staff.DoesNotExist:
                return Response({"detail": "Requesting worker not found."}, status=status.HTTP_404_NOT_FOUND)

        if status_filter:
            reassignments = reassignments.filter(status=status_filter)
        
        serializer = ReassignmentSerializer(reassignments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ReassignmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def reassignment_detail(request, pk):
    reassignment = get_object_or_404(Reassignment, pk=pk)

    if request.method == 'GET':
        serializer = ReassignmentSerializer(reassignment)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ReassignmentSerializer(reassignment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        serializer = ReassignmentSerializer(reassignment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        reassignment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
