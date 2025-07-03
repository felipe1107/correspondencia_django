from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from correspondencia_app.views import CustomLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Login y logout
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),

    # Aplicación principal
    path('', include(('correspondencia_app.urls', 'correspondencia_app'), namespace='correspondencia_app')),
]

# Archivos multimedia en modo desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
