from django.forms import ModelForm
from .models import categoria

class categoriaForm(ModelForm):
    class Meta:
        model = categoria
        fields = ['nombre_categoria']