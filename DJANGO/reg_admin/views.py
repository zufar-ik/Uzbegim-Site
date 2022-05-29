from django.shortcuts import render, redirect
from django.views.generic import DetailView

from .forms import Reg, Update
from .models import Registration, Rooms
import datetime


def view(request):
    form = Reg
    if request.method == 'POST':
        form = Reg(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect('/admin/reg_admin/registration/')
    return render(request,'reg_admin/admin_pan.html',{'form':form})



class Deta(DetailView):
    model = Registration
    template_name = 'reg_admin/all_room.html'
    context_object_name = 'rooms'

# def upd(request):
#     form = Update
#     if request.method == 'POST':
#         form = Reg(request.POST, request.FILES)
#         if form.is_valid():
#             form.instance.author = request.user
#             form.save()
#             return redirect('/admin/reg_admin/registration/')
#     return render(request,'reg_admin/admin_pan.html',{'form':form})
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

def price(request,pk):
    reg = Registration.objects.get(id=pk)
    a = (reg.leave_date)
    b= (reg.visit_date)
    date_1 = datetime.datetime.strptime(str(a),'%Y-%m-%d')
    date_2 = datetime.datetime.strptime(str(b),'%Y-%m-%d')
    result = (date_1 - date_2).days
    if result == 0:
        print(result+reg.price)
        c = int(result) + int(reg.price)
        return c
    elif result >= 1:
        g = int(result) * int(reg.price)
        return g
