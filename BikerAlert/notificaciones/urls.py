from django.urls import path
from . import views

urlpatterns = [
    path('notificaciones/', views.lista_notificaciones, name='lista_notificaciones'),
    path('crear_notificacion/', views.crear_notificacion, name='crear_notificacion')
]