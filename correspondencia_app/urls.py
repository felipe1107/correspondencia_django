from django.urls import path
from . import views

urlpatterns = [
    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),

    # Entradas
    path('entradas/', views.entrada_list, name='entrada_list'),
    path('entradas/crear/', views.crear_entrada, name='crear_entrada'),
    path('entradas/<int:pk>/editar/', views.editar_entrada, name='editar_entrada'),
    path('entradas/<int:pk>/eliminar/', views.eliminar_entrada, name='eliminar_entrada'),

    # Salidas
    path('salidas/', views.salida_list, name='salida_list'),
    path('salidas/crear/', views.crear_salida, name='crear_salida'),
    path('salidas/<int:pk>/editar/', views.editar_salida, name='editar_salida'),
    path('salidas/<int:pk>/eliminar/', views.eliminar_salida, name='eliminar_salida'),

    # Gestores
    path('gestores/', views.gestor_list, name='gestor_list'),
    path('gestores/crear/', views.crear_gestor, name='crear_gestor'),
    path('gestores/<int:pk>/editar/', views.editar_gestor, name='editar_gestor'),
    path('gestores/<int:pk>/eliminar/', views.eliminar_gestor, name='eliminar_gestor'),

    # Logout
    path('logout/', views.logout_view, name='logout'),
]
