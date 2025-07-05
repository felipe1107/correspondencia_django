from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),

    # Usuarios
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),

    # Entradas
    path('entradas/', views.lista_entradas, name='lista_entradas'),
    path('entradas/nueva/', views.crear_entrada, name='crear_entrada'),
    path('entradas/<int:pk>/editar/', views.editar_entrada, name='editar_entrada'),
    path('entradas/<int:pk>/eliminar/', views.eliminar_entrada, name='eliminar_entrada'),

    # Salidas
    path('salidas/', views.lista_salidas, name='lista_salidas'),
    path('salidas/nueva/', views.crear_salida, name='crear_salida'),
    path('salidas/<int:pk>/editar/', views.editar_salida, name='editar_salida'),
    path('salidas/<int:pk>/eliminar/', views.eliminar_salida, name='eliminar_salida'),

    # Gestores
    path('gestores/', views.lista_gestores, name='lista_gestores'),

    # Login
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
