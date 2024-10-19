from django.shortcuts import render, redirect
from .models import Motocicleta
from .forms import MotocicletaForm
# Create your views here.

def lista_motocicletas(request):
    motocicletas = Motocicleta.objects.all()
    return render(request, 'motocicleta/lista_motocicletas.html', {'motocicletas': motocicletas})

def crear_motocicleta(request):
    if request.method == 'POST':
        form = MotocicletaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_motocicletas')
    else:
        form = MotocicletaForm()
        return render(request, 'motocicleta/crear_motocicleta.html', {'form':form})