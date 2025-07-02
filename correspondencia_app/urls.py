from django.urls import path
from . import views

app_name = 'correspondencia_app'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('entradas/', views.entrada_list, name='entrada_list'),
    path('salidas/', views.salida_list, name='salida_list'),
    path('gestores/', views.gestor_list, name='gestor_list'),
    path('entradas_por_mes/', views.entradas_por_mes, name='entradas_por_mes'),
    path('salidas_por_mes/', views.salidas_por_mes, name='salidas_por_mes'),
]
