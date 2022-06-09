#from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .models import Anime
from .serializers import AnimeSerializer

@csrf_exempt
@api_view(['GET'])
def listar_animes(request):
    animes = Anime.objects.all()
    serializer = AnimeSerializer(animes, many=True)
    return Response(serializer.data)
    
@csrf_exempt
@api_view(['POST'])
def agregarAnime(request):
    anime = Anime.objects.create(
            nombre=request.POST['nombre'],
            capitulos=request.POST['capitulos'],
            imagen=request.POST['imagen']
        )
    anime.save()
    return Response([{"mensaje": "Se Agrego Correctamente"}])

@csrf_exempt
@api_view(['PUT'])
def editarAnime(request, p_id):
    try:
        anime = Anime.objects.get(id=p_id)
    
        anime.nombre = request.POST['nombre']
        anime.capitulos = request.POST['capitulos']
        anime.imagen = request.POST['imagen']
        
        anime.save()
        
        return Response([{"mensaje": "Se Modifico Correctamente"}])
    
    except Anime.DoesNotExist:
        return Response(Anime.errors, status=status.HTTP_400_BAD_REQUEST)
    
@csrf_exempt
@api_view(['DELETE'])
def eliminarAnime(request, p_id):
    try:
        anime = Anime.objects.get(id=p_id)
        
        anime.delete()
        return Response([{"mensaje": "Se Elimino Correctamente"}])
        
    except Anime.DoesNotExist:
        return Response(Anime.errors, status=status.HTTP_400_BAD_REQUEST)