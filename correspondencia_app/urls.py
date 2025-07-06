from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('entradas/', views.lista_entradas, name='lista_entradas'),
    path('salidas/', views.lista_salidas, name='lista_salidas'),
    path('gestores/', views.lista_gestores, name='lista_gestores'),  # 👈 Ruta necesaria
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
]
