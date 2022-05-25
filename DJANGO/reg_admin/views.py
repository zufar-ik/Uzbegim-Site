from .models import Registration, Rooms
import datetime


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