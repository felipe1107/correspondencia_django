from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import (
    CustomLoginView,
    entrada_list,
    salida_list,
    gestor_list,
    crear_entrada,
    crear_salida,
    crear_gestor
)

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    path('', entrada_list, name='home'),
    path('entradas/', entrada_list, name='entrada_list'),
    path('salidas/', salida_list, name='salida_list'),
    path('gestores/', gestor_list, name='gestor_list'),

    path('entradas/crear/', crear_entrada, name='crear_entrada'),
    path('salidas/crear/', crear_salida, name='crear_salida'),
    path('gestores/crear/', crear_gestor, name='crear_gestor'),
]
