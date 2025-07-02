from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('correspondencia_app.urls', 'correspondencia_app'), namespace='correspondencia_app')),
    path('login/', auth_views.LoginView.as_view(template_name='correspondencia_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
