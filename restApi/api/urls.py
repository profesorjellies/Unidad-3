from django.urls import path
from .views import listar_animes, agregarAnime, editarAnime, eliminarAnime

urlpatterns = [
    path('listar/', listar_animes, name='home'),
    path('agregar/', agregarAnime),
    path('editarAnime/<p_id>', editarAnime),
    path('eliminarAnime/<p_id>', eliminarAnime)
]
