from django.urls import path, include
from . import views

app_name = 'correspondencia_app'

urlpatterns = [
    # Autenticación
    path('login/',  views.login_view,  name='login'),
    path('logout/', views.logout_view, name='logout'),
    # Dashboard
    path('',         views.dashboard,           name='dashboard'),

    # Entradas
    path('entradas/',               views.entrada_list,    name='entrada_list'),
    path('entradas/nuevo/',         views.entrada_create,  name='entrada_create'),
    path('entradas/<int:pk>/editar/',   views.entrada_edit,    name='entrada_edit'),
    path('entradas/<int:pk>/eliminar/', views.entrada_delete,  name='entrada_delete'),

    # Gestores / Document Managers
    path('gestores/',               views.document_manager_list,   name='document_manager_list'),
    path('gestores/nuevo/',         views.document_manager_create, name='document_manager_create'),
    path('gestores/<int:pk>/editar/',   views.document_manager_edit,   name='document_manager_edit'),
    path('gestores/<int:pk>/eliminar/', views.document_manager_delete, name='document_manager_delete'),
]
