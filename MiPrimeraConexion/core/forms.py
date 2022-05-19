from dataclasses import fields
from django.forms import ModelForm
from .models import Tarea

class FormTarea(ModelForm):
    class Meta:
        model = Tarea
        fields = ['nombre', 'descripcion', 'categoria']

