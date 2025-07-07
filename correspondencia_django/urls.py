from django.contrib import admin
from django.urls import path, include
from correspondencia_app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Vista de login personalizada
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Enlace a las demás URLs de la app
    path('', include('correspondencia_app.urls')),
]
