from django.shortcuts import render
from .models import tarea
from .forms import FormTarea

# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')

def listarTareas(request):
    tareas = tarea.objects.all()
    
    data = {
        'tareas': tareas
    }

    return render(request, 'tarea/listarTareas.html', data)

def formularioTarea(request):

    data = {
        "form" : FormTarea(),
    }

    if request.method == 'POST':
        formulario = FormTarea(request.POST)

        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Guardado'            
        else:
            data['mensaje'] = "Tuvimos un error al agregar"

    return render(request, 'tarea/agregarTarea.html', data)

