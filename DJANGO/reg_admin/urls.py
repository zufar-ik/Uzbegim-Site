from django.urls import path

from .views import obj, time

urlpatterns = [
  path("get/by/<int:pk>/", obj,name='adm'),
  path("get/b/<int:pk>/", time,name='adm')
    ]