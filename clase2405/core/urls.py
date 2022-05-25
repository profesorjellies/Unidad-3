from django.urls import path
from .views import home, listarAnimes

urlpatterns = [
    path('', home, name="inicio"),
    path('listarAnime', listarAnimes, name="listarAnimes")
]