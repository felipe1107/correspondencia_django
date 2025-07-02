from django.urls import path
from . import views

app_name = 'correspondencia_app'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    # Entradas
    path('entradas/', views.entradas_list, name='entradas_list'),
    path('entradas/nueva/', views.entrada_create, name='entrada_create'),
    path('entradas/<int:pk>/editar/', views.entrada_update, name='entrada_update'),
    path('entradas/<int:pk>/eliminar/', views.entrada_delete, name='entrada_delete'),

    # Salidas
    path('salidas/', views.salidas_list, name='salidas_list'),
    path('salidas/nueva/', views.salida_create, name='salida_create'),
    path('salidas/<int:pk>/editar/', views.salida_update, name='salida_update'),
    path('salidas/<int:pk>/eliminar/', views.salida_delete, name='salida_delete'),

    # API para gráficas
    path('entradas/por_mes/', views.entradas_por_mes, name='entradas_por_mes'),
    path('salidas/por_mes/', views.salidas_por_mes, name='salidas_por_mes'),
]
