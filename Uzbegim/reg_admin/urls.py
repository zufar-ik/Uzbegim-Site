from django.urls import path

from .views import RegList, RegUpdater, RegCreate, RegDetail, some_view

urlpatterns = [
    path('all_rooms/', RegList.as_view(), name='view'),
    path('add_room/',RegCreate.as_view(),name='create'),
    path('put_room/<int:pk>', RegUpdater.as_view(), name='update'),
    path('deteil_room/<int:pk>',RegDetail.as_view(),name='detail'),
    path('pdf/',some_view,name='pdf')
]
