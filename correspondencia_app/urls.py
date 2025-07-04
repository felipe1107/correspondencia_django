from django.urls import path
from . import views

urlpatterns = [
    path('', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.cerrar_sesion, name='logout'),

    path('entradas/', views.entrada_list, name='entrada_list'),
    path('entradas/crear/', views.crear_entrada, name='crear_entrada'),
    path('entradas/editar/<int:entrada_id>/', views.editar_entrada, name='editar_entrada'),
    path('entradas/eliminar/<int:entrada_id>/', views.eliminar_entrada, name='eliminar_entrada'),

    path('salidas/', views.salida_list, name='salida_list'),
    path('salidas/crear/', views.crear_salida, name='crear_salida'),
    path('salidas/editar/<int:salida_id>/', views.editar_salida, name='editar_salida'),
    path('salidas/eliminar/<int:salida_id>/', views.eliminar_salida, name='eliminar_salida'),

    path('gestores/', views.gestor_list, name='gestor_list'),
    path('gestores/crear/', views.crear_gestor, name='crear_gestor'),
]
