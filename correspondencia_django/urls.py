# correspondencia_django/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('administración/', admin.site.urls),
    path('', include(('correspondencia_app.urls', 'correspondencia_app'),
                     namespace='correspondencia_app')),
]
