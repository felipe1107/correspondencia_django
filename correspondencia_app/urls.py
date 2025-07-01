from django.urls import path
from . import views

app_name = 'correspondencia_app'

urlpatterns = [
    # Dashboard
    path('',             views.dashboard_stats,             name='dashboard_stats'),

    # Autenticación
    path('login/',       views.login_view,                  name='login'),
    path('logout/',      views.logout_view,                 name='logout'),

    # Entradas
    path('entradas/',                views.EntradaListView.as_view(),   name='entrada_list'),
    path('entradas/nuevo/',          views.EntradaCreateView.as_view(), name='entrada_create'),
    path('entradas/<int:pk>/editar/',views.EntradaUpdateView.as_view(), name='entrada_edit'),
    path('entradas/<int:pk>/eliminar/',views.EntradaDeleteView.as_view(), name='entrada_delete'),

    # Gestores
    path('gestores/',                views.DocumentManagerListView.as_view(),   name='document_manager_list'),
    path('gestores/nuevo/',          views.DocumentManagerCreateView.as_view(), name='document_manager_create'),
    path('gestores/<int:pk>/editar/',views.DocumentManagerUpdateView.as_view(), name='document_manager_edit'),
    path('gestores/<int:pk>/eliminar/',views.DocumentManagerDeleteView.as_view(), name='document_manager_delete'),
]
