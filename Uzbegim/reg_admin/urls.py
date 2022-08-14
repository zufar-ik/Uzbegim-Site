from django.urls import path

from .views import RegList, RegUpdater, RegCreate, RegDetail

urlpatterns = [
    path('all_rooms/', RegList.as_view(), name='view'),
    path('booking/',RegCreate.as_view(),name='create'),
    path('fix/<int:pk>', RegUpdater.as_view(), name='update'),
    path('detail_room/<int:pk>',RegDetail.as_view(),name='detail'),
]
