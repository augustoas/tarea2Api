from django.db import models

# Create your models here.

class Ingrediente(models.Model):
    nombre = models.CharField(null= True, blank= True,max_length=100)
    descripcion = models.CharField(max_length=1000)

class Hamburguesa(models.Model):
    nombre = models.CharField(max_length=2000)
    precio = models.IntegerField()
    descripcion = models.CharField(max_length=2000)
    imagen = models.CharField(max_length=2000)
    ingredientes = models.ManyToManyField(Ingrediente, blank=True)
    
