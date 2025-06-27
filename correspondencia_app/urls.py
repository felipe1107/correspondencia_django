from django.urls import path
from . import views

app_name = 'correspondencia_app'

urlpatterns = [
    # LOGIN / LOGOUT
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # DASHBOARD
    path('', views.dashboard, name='dashboard'),

    # ENTRADAS
    path('entradas/', views.entrada_list, name='entrada_list'),
    path('entradas/nuevo/', views.entrada_create, name='entrada_create'),

    # GESTORES
    path('gestores/', views.document_manager_list, name='document_manager_list'),
    path('gestores/nuevo/', views.document_manager_create, name='document_manager_create'),
]
