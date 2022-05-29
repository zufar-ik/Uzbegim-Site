from django.urls import path

from .views import obj, time, price, view, Deta

urlpatterns = [
  path("get/by/<int:pk>/", obj,name='adm'),
  path("get/b/<int:pk>/", time,name='adm'),
  path('get/<int:pk>/',price),
  path('admin_pan/',view,name='add'),
  # path('admin_pa/',upd,name='dd'),
  path('get/<int:pk>/',Deta.as_view(),name='qq')
    ]