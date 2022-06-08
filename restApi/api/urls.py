from django.urls import path
from .views import listar_animes

urlpatterns = [
    path('listar/', listar_animes, name='home')
]
