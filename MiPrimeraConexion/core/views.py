from django.shortcuts import render, redirect
from .models import Tarea
from .forms import FormTarea

# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')

def listarTareas(request):
    tareas = Tarea.objects.all()
    
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

def editarTarea(request, id):
    
    tarea = Tarea.objects.get(id_tarea = id)
    
    data = {
        'form': FormTarea(instance=tarea)
    }
    
    if request.method == 'POST':
        formulario = FormTarea(data=request.POST, instance=tarea)

        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Modificado'          
        else:
            data['mensaje'] = "Tuvimos un error al modificar"
    
    return render(request, 'tarea/editarTarea.html', data)

def eliminarTarea(request, id):
    tarea = Tarea.objects.get(id_tarea = id)
    tarea.delete()
    
    return redirect(to="listarTareas")