from django.urls import path
from . import views

app_name = 'correspondencia_app'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('entradas/', views.entrada_list, name='entrada_list'),
    path('gestores/', views.document_manager_list, name='document_manager_list'),
     path('logout/', views.logout_view, name='logout'),
    # … demás rutas …
]
