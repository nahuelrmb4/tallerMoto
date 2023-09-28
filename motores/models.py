from django.db import models

class Motor(models.Model):
    codigo= models.CharField(max_length=20)
    
def __str__(self):
    return self.codigo
