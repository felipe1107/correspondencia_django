# correspondencia_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    # Entradas
    path('entradas/', views.entrada_list, name='entrada_list'),
    path('entradas/nuevo/', views.entrada_create, name='entrada_create'),
    path('entradas/eliminar/<int:pk>/', views.entrada_delete, name='entrada_delete'),

    # Gestores
    path('gestores/', views.gestor_list, name='gestor_list'),
    path('gestores/nuevo/', views.gestor_create, name='gestor_create'),
    path('gestores/eliminar/<int:pk>/', views.gestor_delete, name='gestor_delete'),

    # Salidas
    path('salidas/', views.salida_list, name='salida_list'),
    path('salidas/nuevo/', views.salida_create, name='salida_create'),
    path('salidas/eliminar/<int:pk>/', views.salida_delete, name='salida_delete'),

    # Login y logout
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
