from django.urls import path
from . import views

app_name = 'correspondencia_app'

urlpatterns = [
    path('login/',  views.login_view,     name='login'),
    path('logout/', views.logout_view,    name='logout'),

    path('',               views.dashboard,     name='dashboard'),

    path('entradas/',       views.entrada_list,   name='entrada_list'),
    path('entradas/nuevo/', views.entrada_create, name='entrada_create'),
    path('entradas/<int:pk>/editar/', views.entrada_edit,   name='entrada_edit'),
    path('entradas/<int:pk>/eliminar/', views.entrada_delete, name='entrada_delete'),

    path('gestores/',       views.gestor_list,   name='gestor_list'),
    path('gestores/nuevo/', views.gestor_create, name='gestor_create'),
    path('gestores/<int:pk>/editar/',   views.gestor_edit,   name='gestor_edit'),
    path('gestores/<int:pk>/eliminar/', views.gestor_delete, name='gestor_delete'),
]
