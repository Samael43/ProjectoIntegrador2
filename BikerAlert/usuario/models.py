from django.db import models
from django.contrib.auth.models import AbstractUser 

# Create your models here.

class Usuario(AbstractUser):
    nombre = models.CharField(max_length=100)
    dni = models.CharField(max_length=10, unique=True)
    telefono = models.CharField(max_length=20)
    direccion = models.TextField(blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"