from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from correspondencia_app.views import CustomLoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('correspondencia_app.urls', 'correspondencia_app'), namespace='correspondencia_app')),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='/login/'), name='logout'),
]
