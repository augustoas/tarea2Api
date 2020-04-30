from rest_framework import serializers
from .models import Hamburguesa, Ingrediente

class HamburguesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hamburguesa
        fields = ['pk', 'nombre', 'precio', 'descripcion', 'imagen', 'ingredientes']
        read_only_fields = ('pk', 'ingredientes')

class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = ['pk', 'nombre', 'descripcion']

