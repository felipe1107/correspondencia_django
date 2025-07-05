from django.urls import path
from . import views

urlpatterns = [
    path('', views.vista_principal, name='vista_principal'),

    # Usuarios
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),

    # Entradas
    path('entradas/', views.lista_entradas, name='lista_entradas'),
    path('entradas/nueva/', views.crear_entrada, name='crear_entrada'),
    path('entradas/editar/<int:pk>/', views.editar_entrada, name='editar_entrada'),
    path('entradas/eliminar/<int:pk>/', views.eliminar_entrada, name='eliminar_entrada'),

    # Salidas
    path('salidas/', views.lista_salidas, name='lista_salidas'),

    # Gestores
    path('gestores/', views.lista_gestores, name='lista_gestores'),
]
