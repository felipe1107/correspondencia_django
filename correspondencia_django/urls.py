from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('dashboard'), name='root'),
    path('', include('correspondencia_app.urls')),
    path('admin/', admin.site.urls),
]
