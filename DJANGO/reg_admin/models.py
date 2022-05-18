from django.db import models

from django.contrib.auth.models import User


class Ralevant(models.Model):
    bool_roo = models.BooleanField(default=True)


class Rooms(models.Model):
    room_num = models.IntegerField()
    room_bool = models.ForeignKey(Ralevant, on_delete=models.CASCADE,
                                  related_name='name1')  # это надо соединить с моделью Registration
    category = models.CharField(max_length=150)


class Registration(models.Model):
    rooms = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    pasport_serial_num = models.CharField(max_length=100)
    birth_date = models.DateField()
    img = models.FileField()
    visit_date = models.DateTimeField()
    leave_date = models.DateTimeField()
    guest_count = models.IntegerField()
    room_bool = models.ForeignKey(Ralevant, on_delete=models.CASCADE,
                                  related_name='name2')  # это надо соединить с моделью Registration
