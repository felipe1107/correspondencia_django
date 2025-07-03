# correspondencia_django/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('correspondencia_app.urls', namespace='correspondencia_app')),
]
