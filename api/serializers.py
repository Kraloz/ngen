from .models import Planta, Cultivo, Germinacion
from rest_framework import serializers

#serializers.HyperlinkedModelSerializer
class PlantaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Planta
    fields =  ('id', 'nombre', 'dias_germinacion', 'maceta_litros', 'riego', 'etapa_recoleccion', 'extra')


class CultivoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Cultivo
    fields = '__all__'


class GerminacionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Germinacion
    fields = '__all__'
