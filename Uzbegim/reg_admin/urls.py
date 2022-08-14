from django.urls import path

from .views import RegList, RegUpdater, RegCreate, RegDetail, RoomRel

urlpatterns = [
    path('rooms/', RegList.as_view(), name='view'),
    path('booking/', RegCreate.as_view(), name='create'),
    path('fix/<int:pk>', RegUpdater.as_view(), name='update'),
    path('rooms/<int:pk>', RegDetail.as_view(), name='detail'),
    path('relevant/', RoomRel.as_view(), name='all')
]

