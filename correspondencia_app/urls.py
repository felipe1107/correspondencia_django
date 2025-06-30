from django.urls import path
from . import views

app_name = 'correspondencia_app'

urlpatterns = [
    # Autenticación
    path('login/',  views.login_view,       name='login'),
    path('logout/', views.logout_view,      name='logout'),

    # Dashboard de estadísticas
    path('',        views.dashboard_stats,  name='dashboard_stats'),

    # Entradas
    path('entradas/',                 views.entrada_list,         name='entrada_list'),
    path('entradas/nuevo/',           views.entrada_create,       name='entrada_create'),
    path('entradas/<int:pk>/editar/', views.entrada_edit,         name='entrada_edit'),
    path('entradas/<int:pk>/eliminar/',views.entrada_delete,       name='entrada_delete'),
    path('entradas/exportar-csv/',    views.export_entradas_csv,  name='export_entradas_csv'),
    path('entradas/exportar-xlsx/',   views.export_entradas_xlsx, name='export_entradas_xlsx'),

    # Gestores
    path('gestores/',                 views.document_manager_list,   name='document_manager_list'),
    path('gestores/nuevo/',           views.document_manager_create, name='document_manager_create'),
    path('gestores/<int:pk>/editar/', views.document_manager_edit,   name='document_manager_edit'),
    path('gestores/<int:pk>/eliminar/',views.document_manager_delete, name='document_manager_delete'),
    path('gestores/exportar-csv/',    views.export_gestores_csv,     name='export_gestores_csv'),
    path('gestores/exportar-xlsx/',   views.export_gestores_xlsx,    name='export_gestores_xlsx'),
    # justo después de las demás rutas
    path('debug/entradas/', views.debug_entradas, name='debug_entradas'),
]
