# correspondencia_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),

    # Login / Logout
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Gestores
    path('gestores/', views.gestor_list, name='gestor_lista'),
    path('gestores/nuevo/', views.gestor_create, name='gestor_nuevo'),
    path('gestores/eliminar/<int:pk>/', views.gestor_delete, name='gestor_eliminar'),

    # Correspondencia Entrante
    path('entradas/', views.entrada_list, name='entrada_lista'),
    path('entradas/nuevo/', views.entrada_create, name='entrada_nueva'),
    path('entradas/eliminar/<int:pk>/', views.entrada_delete, name='entrada_eliminar'),

    # Correspondencia Saliente
    path('salidas/', views.salida_list, name='salida_lista'),
    path('salidas/nuevo/', views.salida_create, name='salida_nueva'),
    path('salidas/eliminar/<int:pk>/', views.salida_delete, name='salida_eliminar'),
]
