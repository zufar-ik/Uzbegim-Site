from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework import viewsets

from .models import UserReg, UserRoom, UserImg
from .serializers import User, UserRoomSer, UserImgSer, AllRooms


class RoomList(ListAPIView):
    permission_classes = [AllowAny]
    queryset = UserRoom.objects.all()
    serializer_class = AllRooms


class UserRoomViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [AllowAny]
    queryset = UserRoom.objects.all()
    serializer_class = UserRoomSer


class UserCreate(CreateAPIView):
    permission_classes = [AllowAny]
    queryset = UserReg.objects.all()
    serializer_class = User


