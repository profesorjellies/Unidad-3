from dataclasses import fields
from django.forms import ModelForm
from .models import tarea

class FormTarea(ModelForm):
    class Meta:
        model = tarea
        fields = ['nombre', 'descripcion', 'categoria']

