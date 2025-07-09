from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Login de Django con plantilla personalizada
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),

    # Logout de Django con redirección al login
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    # Tu aplicación principal
    path('', include(('correspondencia_app.urls', 'correspondencia_app'), namespace='correspondencia_app')),
]
