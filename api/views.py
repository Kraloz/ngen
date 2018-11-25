from django.shortcuts import render
from rest_framework import viewsets

from .models import Planta, Cultivo, Germinacion
from api.serializers import PlantaSerializer, CultivoSerializer, GerminacionSerializer


class PlantaViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows users to be viewed or edited.
  """
  queryset = Planta.objects.all()
  serializer_class = PlantaSerializer


class CultivoViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows groups to be viewed or edited.
  """
  queryset = Cultivo.objects.all().order_by('-fecha_inicio')
  serializer_class = CultivoSerializer


class GerminacionViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows groups to be viewed or edited.
  """
  queryset = Germinacion.objects.all().order_by('-fecha_inicio')
  serializer_class = GerminacionSerializer