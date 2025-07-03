from django.urls import path
from . import views

app_name = 'correspondencia_app'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('entradas/', views.entrada_list, name='entradas_list'),
    path('entradas/nueva/', views.entrada_create, name='entrada_create'),
    path('salidas/', views.salida_list, name='salidas_list'),
    path('salidas/nueva/', views.salida_create, name='salida_create'),
    path('gestores/', views.gestor_list, name='gestores_list'),
    path('gestores/nuevo/', views.gestor_create, name='gestor_create'),
]
