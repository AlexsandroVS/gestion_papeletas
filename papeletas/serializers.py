from rest_framework import serializers
from .models import Conductor, Infraccion, Papeleta

class ConductorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conductor
        fields = ['id', 'nombre', 'licencia', 'direccion', 'telefono', 'imagen']  # Incluir el campo 'imagen'

class InfraccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Infraccion
        fields = ['id', 'descripcion']

class PapeletaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Papeleta
        fields = ['id', 'conductor', 'infraccion', 'fecha']
