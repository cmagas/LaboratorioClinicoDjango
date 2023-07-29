from django.db import models

# Create your models here.
class analisis(models.Model):
    analisis_id = models.AutoField(primary_key=True);
    analisis_nombre = models.CharField(max_length=50);
    analisis_fregistro = models.DateTimeField(auto_now_add=True);
    analisis_estado = models.BooleanField(default=True);

class especialidad(models.Model):
    especialidad_id = models.AutoField(primary_key=True);
    especialidad_nombre = models.CharField(max_length=50);
    especialidad_fregistro = models.DateTimeField(auto_now_add=True);
    especialidad_estado = models.BooleanField(default=True);

class examen(models.model):
    examen_id = models.AutoField(primary_key=True);
    examen_nombre = models.CharField(max_length=50);
    examen_fregistro = models.DateTimeField(auto_now_add=True);
    analisis_id = models.ForeignKey(analisis, on_delete=models.CASCADE);
    examen_estado = models.BooleanField(default=True);

class medico(models.Model):
    medico_id = models.AutoField(primary_key=True);
    medico_nombre = models.CharField(max_length=50);
    medico_apepat = models.CharField(max_length=50);
    medico_apemat = models.CharField(max_length=50);
    medico_direreccion = models.CharField(max_length=50);
    medico_telefono = models.CharField(max_length=8);
    meduco_fecha_nacimiento = models.DateTimeField();
    medico_nrocolegiatura = models.CharField(max_length=8);
    medico_nrodocumento = models.CharField(max_length=8);
    especialidad_id = models.ForeignKey(especialidad, on_delete=models.CASCADE);
    usario_id = models.ForeignKey(usuario, on_delete=models.CASCADE);

class usuario(models.Model):
    usuario_id = models.AutoField(primary_key=True);
    usuario_nombre = models.CharField(max_length=20);
    usuario_contrasenia = models.CharField(max_length=20);
    rol_id = models.ForeignKey(rol, on_delete=models.CASCADE);
    usuario_email = models.CharField(max_length=255);
    usuario_foto = models.CharField(max_length=255);

class rol(models.Model):
    rol_id = models.AutoField(primary_key=True);
    rol_nombre = models.CharField(max_length=20);
    rol_fregistro = models.DateTimeField(auto_now_add=True);
    rol_estado = models.BooleanField(default=True);

class paciente(models.Model):
    paciente_id = models.AutoField(primary_key=True);
    paciente_nombre = models.CharField(max_length=100);
    paciente_apepat = models.CharField(max_length=100);
    paciente_apemat = models.CharField(max_length=100);
    paciente_ine = models.CharField(max_length=18);
    paciente_telefono = models.CharField(max_length=8);
    paciente_edad = models.IntegerField();
