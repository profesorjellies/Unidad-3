from django.urls import path
from .views import agregarTarea, inicio, tarea, formTarea

urlpatterns = [
    path('', inicio, name="inicio"),
    path('tarea', tarea, name="verTareas"),
    path('tareaAgregar', formTarea, name="agregarTarea")
]
