import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import HttpResponse

from .models import Registration, Rooms
from django.db.models import Q, F


@receiver(post_save, sender=Registration)
def create_profile(sender, instance, created,**kwargs):
    if created:
        instance.rooms.room_bool = instance.room_bool
        instance.rooms.save()
        days = (instance.leave_date - instance.visit_date).days
        if days == '0':
            pass
        else:
            instance.price = instance.rooms.price * int(days)
            instance.save()
    elif not created:
        instance.rooms.room_bool = instance.room_bool
        instance.rooms.save()
        days = (instance.leave_date - instance.visit_date).days
        if int(days) == int(0):
            try:
                instance.price = instance.rooms.price
            except RecursionError:
                pass
        else:
            try:
                instance.price = instance.rooms.price * int(days)
                instance.save()
            except RecursionError:
                pass
