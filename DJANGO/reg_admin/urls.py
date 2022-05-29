from django.urls import path
from .views import RegList, RegDetail

urlpatterns = [
    path('<int:pk>/', RegDetail.as_view()),
    path('', RegList.as_view()),
]
