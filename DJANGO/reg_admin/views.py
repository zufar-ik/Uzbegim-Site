from django.shortcuts import render, redirect
from django.views.generic import DetailView
from rest_framework import generics
from .models import Registration
from .serializers import RegSerializer
from .models import Registration, Rooms
import datetime


class RegList(generics.ListCreateAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegSerializer


class RegDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegSerializer


def obj(request, pk):
    reg = Registration.objects.get(pk=pk)
    room = Rooms.objects.get(pk=pk)
    if reg.room_bool == False:
        room.room_bool = False
        room.save()


def time(request, pk):
    date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    reg = Registration.objects.get(rooms_id=pk)
    room = Rooms.objects.get(pk=pk)
    a = reg.leave_date.replace(tzinfo=None) >= datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S').replace(
        tzinfo=None)
    if a != True:
        reg.room_bool = True
        reg.save()
        room.room_bool = True
        room.save()


def price(request, pk):
    reg = Registration.objects.get(id=pk)
    a = (reg.leave_date)
    b = (reg.visit_date)
    date_1 = datetime.datetime.strptime(str(a), '%Y-%m-%d')
    date_2 = datetime.datetime.strptime(str(b), '%Y-%m-%d')
    result = (date_1 - date_2).days
    if result == 0:
        print(result + reg.price)
        c = int(result) + int(reg.price)
        return c
    elif result >= 1:
        g = int(result) * int(reg.price)
        return g
