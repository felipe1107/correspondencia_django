from django.urls import path
from .views import (
    dashboard,
    entrada_list, entrada_create, entrada_edit,
    salida_list, salida_create, salida_edit,
    gestor_list, gestor_create, gestor_edit,
)

urlpatterns = [
    path('', dashboard, name='dashboard'),

    # Entradas
    path('entradas/', entrada_list, name='entrada_list'),
    path('entradas/nueva/', entrada_create, name='entrada_create'),
    path('entradas/editar/<int:pk>/', entrada_edit, name='entrada_edit'),

    # Salidas
    path('salidas/', salida_list, name='salida_list'),
    path('salidas/nueva/', salida_create, name='salida_create'),
    path('salidas/editar/<int:pk>/', salida_edit, name='salida_edit'),

    # Gestores
    path('gestores/', gestor_list, name='gestor_list'),
    path('gestores/nuevo/', gestor_create, name='gestor_create'),
    path('gestores/editar/<int:pk>/', gestor_edit, name='gestor_edit'),
]
