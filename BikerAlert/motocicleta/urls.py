from django.urls import path
from . import views

urlpatterns = [
    path('motocicletas/', views.lista_motocicletas, name='lista_motocicletas'),
    path('crear_motocicleta/', views.crear_motocicleta, name='crear_motocicleta'),
]