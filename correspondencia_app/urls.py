from django.urls import path
from . import views

app_name = 'correspondencia_app'

urlpatterns = [
    # Vistas principales
    path('', views.dashboard, name='dashboard'),

    # Gestores
    path('gestores/', views.gestor_list, name='gestor_list'),
    path('gestores/nuevo/', views.gestor_create, name='gestor_create'),
    path('gestores/eliminar/<int:pk>/', views.gestor_delete, name='gestor_delete'),

    # Entradas
    path('entradas/', views.entrada_list, name='entrada_list'),
    path('entradas/nuevo/', views.entrada_create, name='entrada_create'),

    # Salidas
    path('salidas/', views.salida_list, name='salida_list'),
    path('salidas/nuevo/', views.salida_create, name='salida_create'),

    # Login / Logout
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Gráficas
    path('api/entradas-por-mes/', views.entradas_por_mes, name='entradas_por_mes'),
]
