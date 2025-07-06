from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('entradas/', views.lista_entradas, name='lista_entradas'),
    path('entradas/nueva/', views.nueva_entrada, name='nueva_entrada'),
    path('entradas/<int:pk>/eliminar/', views.eliminar_entrada, name='eliminar_entrada'),
    path('gestores/', views.lista_gestores, name='lista_gestores'),
]
