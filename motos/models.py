from django.db import models
from motores.models import Motor

class M(models.Model):
    nombre= models.CharField(max_length=100)
    marca=models.CharField(max_length=100)
    modelo=models.CharField(max_length=100)#str es charfield
    cilindrada=models.IntegerField()#int usar integerfield
    fecha_time= models.DateTimeField(auto_now=True)
    motor = models.OneToOneField(Motor, on_delete=models.CASCADE, null=True, blank = True)

def __str__(self):
    return self.nombre

class Mecanico(models.Model):
    nombre=models.CharField(max_length=50)

class Reparacion(models.Model):
    descripccion=models.CharField(max_length=50)
    mecanico=models.ForeignKey(Mecanico, on_delete=models.CASCADE)
    


