from django.urls import path
from . import views

urlpatterns = [
    path('', views.vista_principal, name='vista_principal'),

    # Usuarios
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),

    # Entradas
    path('entradas/', views.lista_entradas, name='lista_entradas'),

    # Salidas
    path('salidas/', views.lista_salidas, name='lista_salidas'),

    # Gestores
    path('gestores/', views.lista_gestores, name='lista_gestores'),
]
