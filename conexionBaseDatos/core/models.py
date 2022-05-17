from django.db import models

# Create your models here.
class categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre_categoria = models.CharField(max_length=50)
    

class tarea(models.Model):
    id_tarea = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    id_categoria = models.ForeignKey(categoria, on_delete=models.CASCADE)

