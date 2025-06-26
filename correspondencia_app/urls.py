from django.urls import path
from . import views

app_name = 'correspondencia_app'

urlpatterns = [
    path('login/',    views.login_view,               name='login'),
    path('logout/',   views.logout_view,              name='logout'),
    path('',          views.dashboard,                name='dashboard'),

    path('entradas/',               views.entrada_list,   name='entrada_list'),
    path('entradas/nuevo/',         views.entrada_create, name='entrada_create'),
    path('entradas/<int:pk>/editar/', views.entrada_edit, name='entrada_edit'),

    path('gestores/',               views.document_manager_list,   name='document_manager_list'),
    path('gestores/nuevo/',         views.document_manager_create, name='document_manager_create'),
    path('gestores/<int:pk>/editar/', views.document_manager_edit,   name='document_manager_edit'),
]
