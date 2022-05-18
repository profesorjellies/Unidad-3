from django.urls import path
from .views import inicio, listarTareas, formularioTarea

urlpatterns = [
    path('', inicio, name="inicio"),
    path('listarTareas', listarTareas, name="listarTareas"),
    path('formularioAgregar', formularioTarea)
]