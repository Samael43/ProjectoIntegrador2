from django.db import models

# Create your models here.

class Motocicleta(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    año = models.IntegerField()
    cilindrada = models.IntegerField()
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.año})"