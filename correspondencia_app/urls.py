from django.urls import path
from . import views

app_name = 'correspondencia_app'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    # Login / logout
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Entradas
    path('entradas/', views.entrada_list, name='entrada_list'),
    path('entradas/nuevo/', views.entrada_create, name='entrada_create'),
    path('entradas/editar/<int:pk>/', views.entrada_edit, name='entrada_edit'),
    path('entradas/eliminar/<int:pk>/', views.entrada_delete, name='entrada_delete'),

    # Gestores
    path('gestores/', views.gestor_list, name='gestor_list'),
    path('gestores/nuevo/', views.gestor_create, name='gestor_create'),
    path('gestores/editar/<int:pk>/', views.gestor_edit, name='gestor_edit'),
    path('gestores/eliminar/<int:pk>/', views.gestor_delete, name='gestor_delete'),
]
