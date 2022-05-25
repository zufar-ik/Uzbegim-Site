import datetime

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Registration


@receiver(post_save, sender=Registration)
def create_profile(sender, instance, created, **kwargs):
    if created:
        instance.rooms.room_bool = False
        instance.rooms.save()
