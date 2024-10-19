from django import forms
from .models import Motocicleta


class MotocicletaForm(forms.ModelForm):
    class Meta:
        model = Motocicleta
        fields = ('modelo', 'marca', 'año')