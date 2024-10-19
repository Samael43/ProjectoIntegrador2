from django.db import models

# Create your models here.

class TipoMantenimiento(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class Mantenimiento(models.Model):
    motocicleta = models.ForeignKey('motocicleta.Motocicleta', on_delete=models.CASCADE)
    tipo_mantenimiento = models.ForeignKey(TipoMantenimiento, on_delete=models.CASCADE)
    fecha_realizacion = models.DateField()
    proxima_fecha_realizacion = models.DateField(blank=True, null=True)
    observaciones = models.TextField(blank=True)

    def __str__(self):
        return f"Mantenimiento {self.tipo_mantenimiento.nombre} de {self.motocicleta}"