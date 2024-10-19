from django.shortcuts import render, redirect
from .models import Notificacion
from .forms import NotificacionForm

# Create your views here.

def lista_notificaciones(request):
    notificaciones = Notificacion.objects.all()
    return render(request, 'notificaciones/lista_notificaciones.html', {'notificaciones': notificaciones})

def crear_notificacion(request):
    if request.method == 'POST':
        form = NotificacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_notificaciones')
        
    else:
        form= NotificacionForm()
        return render(request, 'notificaciones/crear_notificacion.html', {'form':form})
