from django.shortcuts import redirect, render
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

def agregarAnime(request):
    
    data = {
        'mensaje': '',
        'mostrar_mensaje': False
    }
    
    if request.method == 'POST':
        Anime.objects.create(
            nombre=request.POST['nombre'],
            capitulos=request.POST['capitulo'],
            imagen=request.POST['imagen']
        )
        data['mostrar_mensaje'] = True
        data['mensaje'] = 'Se Agrego Con Exito'  
    
    return render(request, 'anime/agregarAnime.html', data)

def eliminarAnime(request, id):
    anime = Anime.objects.get(id = id)
    anime.delete()
  
    return redirect('listarAnimes')

def editarAnime(request, id):
    anime = Anime.objects.get(id = id)
    data = {}
    if request.method == 'POST':
        anime.nombre = request.POST['nombre']
        anime.capitulos=request.POST['capitulo']
        anime.imagen=request.POST['imagen']
        anime.save()
        
        data['mensaje'] = 'Actualizado Correctamente'
        data['mostrar_mensaje'] = True
        
    data['anime'] = anime
    
    return render(request, 'anime/editarAnime.html', data)
