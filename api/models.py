from django.db import models

# Create your models here.
class Planta(models.Model):
  nombre = models.CharField(max_length=45)
  dias_germinacion = models.IntegerField()
  maceta_litros = models.IntegerField()
  riego = models.CharField(max_length=150)
  etapa_recoleccion = models.CharField(max_length=150)
  extra = models.TextField(null=True, blank=True)
  def __str__(self):
    return self.nombre


class Cultivo(models.Model):
  fecha_inicio = models.DateField()
  fecha_estimada = models.DateField()
  planta = models.ForeignKey(Planta, on_delete=models.CASCADE)
  def __str__(self):
    return self.planta


class Germinacion(models.Model):
  fecha_inicio = models.DateField()
  fecha_estimada = models.DateField()
  planta = models.ForeignKey(Planta, on_delete=models.CASCADE)
  def __str__(self):
    return self.planta