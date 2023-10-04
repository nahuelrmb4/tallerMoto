from django.db import models

class Marca(models.Model):
    nombre =models.CharField(max_length=30)

class Motor(models.Model):
    codigo= models.CharField(max_length=20)
    marca=models.ManyToManyField(Marca)

    
def __str__(self):
    return self.codigo
