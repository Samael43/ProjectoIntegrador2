from django import forms
from .models import Mantenimiento, TipoMantenimiento

class MantenimientoForm(forms.ModelForm):
    class Meta:
        model = Mantenimiento
        fields = ['motocicleta', 'tipo_mantenimiento', 'fecha_realizacion', 'proxima_fecha_realizacion', 'observaciones']

class TipoMantenimientoForm(forms.ModelForm):
    class Meta:
        model = TipoMantenimiento
        fields = ['nombre', 'descripcion']
