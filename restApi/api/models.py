from django.db import models

# Create your models here.
class Anime(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    capitulos = models.IntegerField()
    imagen = models.CharField(max_length=250)
