from django.urls import path
from .views import listar_animes, agregar_anime

urlpatterns = [
    path('listar/', listar_animes, name='home'),
    path('agregar/', agregar_anime)
]
