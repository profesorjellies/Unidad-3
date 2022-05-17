from multiprocessing import context
from django.shortcuts import render
from .models import categoria
from .forms import categoriaForm

# Create your views here.
def home(request):

    ##accedemos al objeto que tiene la informacion
    categorias = categoria.objects.all()

    datos = {
        'categorias': categorias
    }
    return render(request, 'home.html', datos)

def formCategoria(request):
    context = {
        "form" : categoriaForm(),
    }

    if request.method == 'POST':

        formulario = categoriaForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            context['mensaje'] = 'Guardado'
    
    return render(request, 'form_categoria.html', context)