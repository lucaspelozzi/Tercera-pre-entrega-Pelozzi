from django.db import models

# Create your models here.

from django.db import models

class MiModelo(models.Model):
    campo1 = models.CharField(max_length=50)
    campo2 = models.CharField(max_length=50)
    campo3 = models.CharField(max_length=50)
    campo4 = models.CharField(max_length=50)
    
    def __str__(self):
        return self.campo1