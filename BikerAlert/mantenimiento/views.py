from django.shortcuts import render,redirect
from .models import Mantenimiento
from .forms import MantenimientoForm, TipoMantenimientoForm

# Create your views here.

def lista_mantenimientos(request):
    mantenimientos = Mantenimiento.objects.all()
    tipos_mantenimiento = tipos_mantenimiento.objects.all()
    return render(request, 'mantenimiento/lista_mantenimiento.html', {'mantenimientos': mantenimientos, 'tipos_mantenimiento': tipos_mantenimiento})

def crear_mantenimiento(request):
    if request.method == 'POST':
        form = MantenimientoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_mantenimientos')
    else:
        form = MantenimientoForm()
    return render(request, 'mantenimiento/crear_mantenimiento.html', {'form': form})

def crear_tipo_mantenimiento(request):
    if request.method == 'POST':
        form = TipoMantenimientoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_tipos_mantenimiento')
    else:
        form = TipoMantenimientoForm()
    return render(request, 'mantenimiento/crear_tipo_mantenimiento.html', {'form': form})
