from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'correspondencia_app'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='correspondencia_app:login'), name='logout'),
    
    path('entradas/', views.entradas_list, name='entradas_list'),
    path('entradas/nueva/', views.entrada_create, name='entrada_create'),
    path('entradas/<int:pk>/editar/', views.entrada_update, name='entrada_update'),
    path('entradas/<int:pk>/eliminar/', views.entrada_delete, name='entrada_delete'),

    path('salidas/', views.salidas_list, name='salidas_list'),
    path('salidas/nueva/', views.salida_create, name='salida_create'),
    path('salidas/<int:pk>/editar/', views.salida_update, name='salida_update'),
    path('salidas/<int:pk>/eliminar/', views.salida_delete, name='salida_delete'),

    path('gestores/', views.gestores_list, name='gestores_list'),
    path('gestores/nuevo/', views.gestor_create, name='gestor_create'),
    path('gestores/<int:pk>/editar/', views.gestor_update, name='gestor_update'),
    path('gestores/<int:pk>/eliminar/', views.gestor_delete, name='gestor_delete'),
]
