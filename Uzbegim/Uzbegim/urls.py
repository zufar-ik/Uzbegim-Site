from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('super/', include('reg_admin.urls')),
    path('users/', include('reg_user.urls')),
    path('auth/', include('dj_rest_auth.urls')),
    path('reg/',include('dj_rest_auth.registration.urls')),
]
