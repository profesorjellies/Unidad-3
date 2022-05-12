from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'index.html')

def tarea(request):
    data = {
        "name": "Julio", 
        "edad": 28,
        "hobby": "me gusta dormir",
        "lista": ['alumno1', 'alumno2', 'alumno3', 'alumno4', 'alumno5']
    }
    return render(request, 'tareas/tarea.html', data )

def formTarea(request):
    return render(request, 'tareas/formularioTarea.html')

def agregarTarea(request):
    print(request.post['titulo'])
    data = {}
    return render(request, 'tareas/verResultado.html', data)
