from django.contrib import admin
from django.urls import path, include
from correspondencia_app.views import CustomLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='/login/'), name='logout'),
    path('', include(('correspondencia_app.urls', 'correspondencia_app'), namespace='correspondencia_app')),
]
