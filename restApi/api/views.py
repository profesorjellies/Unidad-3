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
# Create your views here.
def listar_animes(request):
    animes = Anime.objects.all()
    serializer = AnimeSerializer(animes, many=True)
    return Response(serializer.data)


def agregar_anime(request):
    data = JSONParser().parse(request)
    print(data)
    if request.method == 'POST':
        data = JSONParser().parse(request)
        print(data)
        serializer = AnimeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
