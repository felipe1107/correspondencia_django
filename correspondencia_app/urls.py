# correspondencia_app/urls.py
from django.urls import path
from . import views

app_name = 'correspondencia_app'

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('', views.dashboard, name='dashboard'),
    path('entradas/', views.entrada_list, name='entrada_list'),
    path('entradas/nueva/', views.entrada_create, name='entrada_create'),
    path('entradas/<int:pk>/editar/', views.entrada_edit, name='entrada_edit'),
    path('salidas/', views.salida_list, name='salida_list'),
    path('salidas/nueva/', views.salida_create, name='salida_create'),
    path('salidas/<int:pk>/editar/', views.salida_edit, name='salida_edit'),
    path('gestores/', views.gestor_list, name='gestor_list'),
    path('gestores/nuevo/', views.gestor_create, name='gestor_create'),
    path('gestores/<int:pk>/editar/', views.gestor_edit, name='gestor_edit'),
]
