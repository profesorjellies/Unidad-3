from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .models import Anime
from .serializers import AnimeSerializer

@csrf_exempt
@api_view(['GET', 'POST'])
def listar_animes(request):
    if request.method == 'GET':
        animes = Anime.objects.all()
        serializer = AnimeSerializer(animes, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        anime = Anime.objects.create(
            id=request.POST['id'],
            nombre=request.POST['nombre'],
            capitulos=request.POST['capitulos'],
            imagen=request.POST['imagen']
        )
        anime.save()
        return Response([{"mensaje": "Se Agrego Correctamente"}])      
    else:
        return Response([{"error": "ok"}])
    



        
























    #     data = JSONParser().parse(request)
        # print(data)
        # serializer = AnimeSerializer(data=data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # else:
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
