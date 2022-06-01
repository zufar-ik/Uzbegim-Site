from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions  # new


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('reg_admin.urls')),
    path('users/', include('reg_user.urls')),

]
