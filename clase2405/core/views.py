from django.shortcuts import render
from .models import Anime

# Create your views here.
def home(request):
    return render(request, 'home.html')

def listarAnimes(request):

    animes = Anime.objects.all

    data = {
        'animes' : animes
    }

    return render(request, 'anime/listarAnime.html', data)
