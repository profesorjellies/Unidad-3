from django.urls import path
from .views import eliminarTarea, inicio, listarTareas, formularioTarea, editarTarea, eliminarTarea

urlpatterns = [
    path('', inicio, name="inicio"),
    path('listarTareas', listarTareas, name="listarTareas"),
    path('formularioAgregar', formularioTarea, name="agregar"),
    path('editarTarea/<id>', editarTarea, name="editar"),
    path('eliminarTarea/<id>', eliminarTarea, name="eliminar")
]