from .views import UserCreate, UserRoomViewSet, RoomList
from django.urls import path
from rest_framework import routers

urlpatterns = [
    path('room/', RoomList.as_view(), name='all_room'),
    path('booking/', UserCreate.as_view(), name='add_room'),
]
#routers
router = routers.DefaultRouter()
router.register(r'room', UserRoomViewSet)
urlpatterns += router.urls
