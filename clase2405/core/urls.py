from django.urls import path
from .views import home, listarAnimes, agregarAnime, eliminarAnime, editarAnime

urlpatterns = [
    path('', home, name="inicio"),
    path('listarAnime', listarAnimes, name="listarAnimes"),
    path('agregarAnime', agregarAnime, name="agregarAnime"),
    path('eliminarAnime/<id>', eliminarAnime, name="eliminarAnime"),
    path('editarAnime/<id>', editarAnime, name="editarAnime")
]