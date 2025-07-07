from django.urls import path
from . import views

urlpatterns = [
    # Autenticación
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Página principal (dashboard)
    path('dashboard/', views.dashboard, name='dashboard'),

    # Entradas
    path('entradas/', views.entrada_list, name='entrada_list'),
    path('entradas/nueva/', views.entrada_create, name='entrada_create'),
    path('entradas/<int:pk>/editar/', views.entrada_update, name='entrada_update'),
    path('entradas/<int:pk>/eliminar/', views.entrada_delete, name='entrada_delete'),

    # Salidas
    path('salidas/', views.salida_list, name='salida_list'),
    path('salidas/nueva/', views.salida_create, name='salida_create'),
    path('salidas/<int:pk>/editar/', views.salida_update, name='salida_update'),
    path('salidas/<int:pk>/eliminar/', views.salida_delete, name='salida_delete'),

    # Gestores
    path('gestores/', views.gestor_list, name='gestor_list'),
    path('gestores/nuevo/', views.gestor_create, name='gestor_create'),
    path('gestores/<int:pk>/editar/', views.gestor_update, name='gestor_update'),
    path('gestores/<int:pk>/eliminar/', views.gestor_delete, name='gestor_delete'),
]
