from django.urls import path
from .views import (
    login_usuario,
    cerrar_sesion,
    registro_usuario,
    vista_principal,
    lista_usuarios,
)

urlpatterns = [
    path('', vista_principal, name='inicio'),
    path('login/', login_usuario, name='login'),
    path('logout/', cerrar_sesion, name='logout'),
    path('registro/', registro_usuario, name='registro'),
    path('usuarios/', lista_usuarios, name='lista_usuarios'),
]
