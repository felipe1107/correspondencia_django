from django.contrib import admin
from django.urls import path, include

urlpatterns = [
   path('', lambda request: redirect('login'), name='root'),
    path('', include('correspondencia_app.urls')),
    path('admin/', admin.site.urls),
]
