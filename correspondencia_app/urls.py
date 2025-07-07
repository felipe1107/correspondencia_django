from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),

    # Entradas
    path('entradas/', views.entrada_list, name='entrada_list'),
    path('entradas/crear/', views.crear_entrada, name='crear_entrada'),
    path('entradas/editar/<int:pk>/', views.editar_entrada, name='editar_entrada'),
    path('entradas/eliminar/<int:pk>/', views.eliminar_entrada, name='eliminar_entrada'),

    # Salidas
    path('salidas/', views.salida_list, name='salida_list'),
    path('salidas/crear/', views.crear_salida, name='crear_salida'),
    path('salidas/editar/<int:pk>/', views.editar_salida, name='editar_salida'),
    path('salidas/eliminar/<int:pk>/', views.eliminar_salida, name='eliminar_salida'),

    # Gestores
    path('gestores/', views.gestor_list, name='gestor_list'),
    path('gestores/crear/', views.crear_gestor, name='crear_gestor'),
    path('gestores/editar/<int:pk>/', views.editar_gestor, name='editar_gestor'),
    path('gestores/eliminar/<int:pk>/', views.eliminar_gestor, name='eliminar_gestor'),

    # Logout
    path('logout/', views.logout_view, name='logout'),
]
