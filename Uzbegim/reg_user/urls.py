from django.urls import path

from .views import UserList, UserCreate, UserDetail

urlpatterns = [
    path('all_room/', UserList.as_view(), name='all_room'),
    path('add_room/', UserCreate.as_view(), name='add_room'),
    path('detail_room/<int:pk>', UserDetail.as_view(), name='detail_room'),
]
