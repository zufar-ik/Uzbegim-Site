import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Registration, Rooms


@receiver(post_save, sender=Registration)
def create_profile(sender, instance, created,**kwargs):
    if created:
        instance.rooms.room_bool = instance.room_bool
        instance.rooms.save()
        instance.price = instance.rooms.price
        instance.save()
    elif not created:
        instance.rooms.room_bool = instance.room_bool
        instance.rooms.save()