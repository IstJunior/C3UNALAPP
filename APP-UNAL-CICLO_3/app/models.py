from email.policy import default
from statistics import mode
from django.db import models
from django.db import models




# Create your models here.
class Familiar(models.Model):
    id = models.AutoField(primary_key=True)
    cedula = models.BigIntegerField(null=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    tel_contacto = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    
    
class Medicos(models.Model):
    id = models.AutoField(primary_key=True)
    cedula = models.BigIntegerField(null=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=50)
    tel_contacto = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    
            
class Pacientes(models.Model):
    id_paciente =models.BigIntegerField(primary_key=True)
    id_familiar_designado = models.ForeignKey(Familiar, on_delete = models.CASCADE)
    id_medico_designado = models.ForeignKey(Medicos, on_delete =models.CASCADE)
    cedula = models.BigIntegerField(null=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    tel_contacto = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    
class HistoriaClinica(models.Model):
    id = models.AutoField(primary_key=True)
    paciente_id  = models.ForeignKey(Pacientes, on_delete = models.CASCADE)
    observaciones = models.TextField(max_length=250)
    
class SignosVitales(models.Model):
    id = models.AutoField(primary_key=True)
    paciente_id = models.ForeignKey(Pacientes, on_delete = models.CASCADE)
    oximetria = models.TextField(max_length=100)
    frecuencia_respiratoria = models.TextField(max_length=100)
    frecuencia_cardiaca = models.TextField(max_length=100)
    
class Usuarios(models.Model):
    rol = models.CharField(max_length=50, null=False)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    tel_contacto = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    

    
    
    
    



