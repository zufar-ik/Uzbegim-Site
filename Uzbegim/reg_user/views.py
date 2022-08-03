from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny

from .models import UserReg, UserRoom, UserImg
from .serializers import User, UserRoomSer


class UserList(ListAPIView):
    permission_classes = [AllowAny]
    queryset = UserRoom.objects.all()
    serializer_class = UserRoomSer


class UserCreate(CreateAPIView):
    permission_classes = [AllowAny]
    queryset = UserReg.objects.all()
    serializer_class = User


class UserDetail(RetrieveAPIView):
    queryset = UserReg.objects.all()
    serializer_class = User
