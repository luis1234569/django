from django.db import models

# Create your models here.

class Tipo_persona (models.Model):
    tipo = models.CharField(max_length=80)  

class Persona (models.Model):
    nombre = models.CharField(max_length=80)
    cedula = models.IntegerField()
    fecha_nacimiento = models.DateField(auto_now=False, auto_now_add=False)
    monto_primera_compra = models.FloatField()
    tipo=models.ForeignKey(Tipo_persona,on_delete=models.PROTECT)
