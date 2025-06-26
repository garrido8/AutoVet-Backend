from rest_framework.response import Response
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser 
from rest_framework import status

from .models import Pet
from .serializers import PetSerializer

@api_view(['GET', 'POST'])
@parser_classes([MultiPartParser, FormParser, JSONParser]) 
def pet_list(request):
    if request.method == 'GET':
        especie = request.query_params.get('especie', None)
        raza = request.query_params.get('raza', None)
        propietario = request.query_params.get('propietario', None)

        pets = Pet.objects.all()

        if especie:
            pets = pets.filter(especie__icontains=especie)
        if raza:
            pets = pets.filter(raza__icontains=raza)
        if propietario:
            pets = pets.filter(propietario_id=propietario)

        serializer = PetSerializer(pets, many=True, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@parser_classes([MultiPartParser, FormParser])
def pet_detail(request, pk):
    try:
        pet = Pet.objects.get(pk=pk)
    except Pet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PetSerializer(pet, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PetSerializer(pet, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        pet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def pets_by_owner(request, propietario):
    pets = Pet.objects.filter(propietario_id=propietario)
    serializer = PetSerializer(pets, context={ 'request': request }, many=True)
    return Response(serializer.data)