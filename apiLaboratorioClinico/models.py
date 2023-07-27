from django.db import models

# Create your models here.
class Analisis(models.Model):
    analisis_id = models.AutoField(primary_key=True);
    analisis_nombre = models.CharField(max_length=50);
    analisis_fregistro = models.DateTimeField(auto_now_add=True);
    analisis_estado = models.BooleanField(default=True);

class especialidad(models.Model):
    especialidad_id = models.AutoField(primary_key=True);
    especialidad_nombre = models.CharField(max_length=50);
    especialidad_fregistro = models.DateTimeField(auto_now_add=True);
    especialidad_estado = models.BooleanField(default=True);

class examen(models.model)
