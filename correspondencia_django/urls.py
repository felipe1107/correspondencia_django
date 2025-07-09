from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Login con plantilla personalizada
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),

    # Logout con redirección al login
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    # Aplicación principal
    path('', include(('correspondencia_app.urls', 'correspondencia_app'), namespace='correspondencia_app')),
]

# Servir archivos multimedia en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
