from django.urls import path
from . import views

app_name = "correspondencia_app"

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('gestores/', views.gestor_list, name='gestor_list'),
    path('gestores/nuevo/', views.gestor_create, name='gestor_create'),
    path('gestores/eliminar/<int:pk>/', views.gestor_delete, name='gestor_delete'),

    path('entradas/', views.entrada_list, name='entrada_list'),
    path('entradas/nuevo/', views.entrada_create, name='entrada_create'),

    path('salidas/', views.salida_list, name='salida_list'),
    path('salidas/nuevo/', views.salida_create, name='salida_create'),

    path('entradas_por_mes/', views.entradas_por_mes, name='entradas_por_mes'),
]
