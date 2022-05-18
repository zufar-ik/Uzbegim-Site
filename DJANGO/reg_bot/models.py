from django.db import models
from ..reg_admin.models import Ralevant


class User(models.Model):
    name = models.CharField(max_length=150)
    username = models.CharField(max_length=150)
rooms_choice = [
    ("101","101"),
    ("201","201"),
    ("202","202"),
    ("203","203"),
    ("204","204"),
    ("205","205"),
    ("206","206"),
    ("207","207"),
    ("208","208"),
    ("209","209"),
    ("210","210"),
    ("211","211"),
    ("301","301"),
]
class Registration(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    rooms = models.CharField(choices=rooms_choice,max_length=150)
    visit_date = models.DateTimeField()
    leave_date = models.DateTimeField()
    tel_num = models.IntegerField()
    count = models.IntegerField(default=1)
    room_bool = models.ForeignKey(Ralevant, on_delete=models.CASCADE,
                                  related_name='name3')  # это надо соединить с моделью Registration
