from django.urls import path
from . import views

urlpatterns = [
    path('mantenimientos/', views.lista_mantenimientos, name='lista_mantenimientos'),
    path('crear_tipo_mantenimiento/', views.crear_tipo_mantenimiento, name='crear_tipo_mantenimiento'),
]