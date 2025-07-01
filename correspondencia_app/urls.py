from django.urls import path
from . import views

app_name = 'correspondencia_app'

urlpatterns = [
    # Autenticación y Dashboard
    path('login/',  views.login_view,       name='login'),
    path('logout/', views.logout_view,      name='logout'),
    path('',        views.dashboard_stats,  name='dashboard_stats'),

    # Entradas CBV
    path('entradas/',                   views.EntradaListView.as_view(),   name='entrada_list'),
    path('entradas/nuevo/',             views.EntradaCreateView.as_view(), name='entrada_create'),
    path('entradas/<int:pk>/editar/',   views.EntradaUpdateView.as_view(), name='entrada_edit'),
    path('entradas/<int:pk>/eliminar/', views.EntradaDeleteView.as_view(), name='entrada_delete'),
    path('entradas/exportar-csv/',      views.export_entradas_csv,          name='export_entradas_csv'),
    path('entradas/exportar-xlsx/',     views.export_entradas_xlsx,         name='export_entradas_xlsx'),

    # Gestores
   path('gestores/',                   views.GestorListView.as_view(),   name='document_manager_list'),
   path('gestores/nuevo/',             views.GestorCreateView.as_view(), name='document_manager_create'),
   path('gestores/<int:pk>/editar/',   views.GestorUpdateView.as_view(), name='document_manager_edit'),
   path('gestores/<int:pk>/eliminar/', views.GestorDeleteView.as_view(), name='document_manager_delete'),

    # Debug
    path('debug/entradas/',             views.debug_entradas,               name='debug_entradas'),
]
