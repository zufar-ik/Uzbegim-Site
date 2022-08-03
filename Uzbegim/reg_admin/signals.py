from django.db.models.signals import post_save
from django.dispatch import receiver
import requests
from .models import Registration, Rooms

from environs import Env

# Используем библиотеку environs
env = Env()
env.read_env()
ADMINS = (env.list('ADMIN_BOT'))  # Список админов


@receiver(post_save, sender=Registration)
def create_profile(sender, instance, created, **kwargs):
    if created:
        instance.rooms.room_bool = instance.room_bool
        instance.rooms.save()
        token = '5419456477:AAH4XGE9O-90vgiDHVTiV2Kmq8JWXiXFRNw'
        URL = 'https://api.telegram.org/bot' + token + '/sendMessage'
        for chat_id in ADMINS:
            try:
                data = {'chat_id': chat_id, 'text': "Забронирован один номер через Ресепшен\n\n"
                                                    "Посмотрите по ссылке http://127.0.0.1:8000/admin/reg_admin/registration/\n\n"
                                                    "Нажмите /start чтобы вывести меню администратора"}
                requests.post(URL, data=data)
            except Exception:
                pass
        days = (instance.leave_date - instance.visit_date).days
        if int(days) == int(0):
            instance.price = instance.rooms.price
            instance.save()
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
