from django.urls import path
from . import views

app_name = 'correspondencia_app'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    # Autenticación
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Entradas
    path('entradas/', views.entrada_list, name='entrada_list'),
    path('entradas/nueva/', views.entrada_create, name='entrada_create'),
    path('entradas/<int:pk>/editar/', views.entrada_edit, name='entrada_edit'),
    path('entradas/<int:pk>/eliminar/', views.entrada_delete, name='entrada_delete'),

    # Salidas
    path('salidas/', views.salida_list, name='salida_list'),
    path('salidas/nueva/', views.salida_create, name='salida_create'),
    path('salidas/<int:pk>/editar/', views.salida_edit, name='salida_edit'),
    path('salidas/<int:pk>/eliminar/', views.salida_delete, name='salida_delete'),

    # Gestores
    path('gestores/', views.gestor_list, name='gestor_list'),
    path('gestores/nuevo/', views.gestor_create, name='gestor_create'),
    path('gestores/<int:pk>/editar/', views.gestor_update, name='gestor_update'),
    path('gestores/<int:pk>/eliminar/', views.gestor_delete, name='gestor_delete'),

    # Página de inicio
    path('inicio/', views.index, name='inicio'),
]
