from django.urls import path
from . import views

app_name = 'correspondencia_app'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('entradas/', views.entrada_list, name='entrada_list'),
    path('entradas/nueva/', views.entrada_create, name='entrada_create'),
    path('entradas/editar/<int:pk>/', views.entrada_update, name='entrada_update'),
    path('entradas/eliminar/<int:pk>/', views.entrada_delete, name='entrada_delete'),

    path('salidas/', views.salida_list, name='salida_list'),
    path('salidas/nueva/', views.salida_create, name='salida_create'),
    path('salidas/editar/<int:pk>/', views.salida_update, name='salida_update'),
    path('salidas/eliminar/<int:pk>/', views.salida_delete, name='salida_delete'),

    path('gestores/', views.gestor_list, name='gestor_list'),
    path('gestores/nuevo/', views.gestor_create, name='gestor_create'),
    path('gestores/editar/<int:pk>/', views.gestor_update, name='gestor_update'),
    path('gestores/eliminar/<int:pk>/', views.gestor_delete, name='gestor_delete'),

    path('entradas_por_mes/', views.entradas_por_mes, name='entradas_por_mes'),
    path('salidas_por_mes/', views.salidas_por_mes, name='salidas_por_mes'),

    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
