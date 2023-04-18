from django.db import models

# Create your models here.

class MiModelo(models.Model):
    
    campo1 = models.CharField(max_length=50)
    campo2 = models.CharField(max_length=50)
    campo3 = models.CharField(max_length=50)
    campo4 = models.CharField(max_length=50)
    
    def __str__(self):
        return self.campo1
    
class Animal(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()

class Persona(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()