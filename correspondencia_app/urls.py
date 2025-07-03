from django.urls import path
from .views import entrada_list

app_name = 'correspondencia_app'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('entradas/', entrada_list, name='entrada_list'),
    path('entradas/crear/', views.entrada_create, name='entrada_create'),
    
    path('salidas/', views.salida_list, name='salida_list'),
    path('salidas/crear/', views.salida_create, name='salida_create'),

    path('gestores/', views.gestor_list, name='gestor_list'),
    path('gestores/crear/', views.gestor_create, name='gestor_create'),
]
