from django.urls import path
from .views import (
    entrada_list,
    crear_entrada,
    editar_entrada,
    eliminar_entrada,
    salida_list,
    crear_salida,
    editar_salida,
    eliminar_salida,
    gestor_list,
    crear_gestor,
    editar_gestor,
    eliminar_gestor,
    cerrar_sesion,
)

urlpatterns = [
    path('entradas/', entrada_list, name='entrada_list'),
    path('entradas/crear/', crear_entrada, name='crear_entrada'),
    path('entradas/editar/<int:pk>/', editar_entrada, name='editar_entrada'),
    path('entradas/eliminar/<int:pk>/', eliminar_entrada, name='eliminar_entrada'),

    path('salidas/', salida_list, name='salida_list'),
    path('salidas/crear/', crear_salida, name='crear_salida'),
    path('salidas/editar/<int:pk>/', editar_salida, name='editar_salida'),
    path('salidas/eliminar/<int:pk>/', eliminar_salida, name='eliminar_salida'),

    path('gestores/', gestor_list, name='gestor_list'),
    path('gestores/crear/', crear_gestor, name='crear_gestor'),
    path('gestores/editar/<int:pk>/', editar_gestor, name='editar_gestor'),
    path('gestores/eliminar/<int:pk>/', eliminar_gestor, name='eliminar_gestor'),

    path('logout/', cerrar_sesion, name='cerrar_sesion'),
]
