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
        if instance.rooms.category != 'President-Lux' and 'Lux':
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
            # один день и один человек!
            if int(days) == int(0) and instance.guest_count == int(1):
                instance.price = instance.rooms.price
                instance.save()
            # один день и два человека!
            elif int(days) == int(0) and instance.guest_count == int(2):
                percent = ((instance.rooms.price) // 100 * 40)
                instance.price = instance.rooms.price + percent
                instance.save()
            # один день и больше двух людей!
            elif int(days) == int(0) and instance.guest_count > int(2):
                percent = ((instance.rooms.price) // 100 * 60)
                instance.price = instance.rooms.price + percent
                instance.save()
            # не один день и один человек!
            elif int(days) != int(0) and instance.guest_count == int(1):
                instance.price = (instance.rooms.price * int(days))
                instance.save()

            # не один день и 2 человека!
            elif int(days) != int(0) and instance.guest_count == int(2):
                percent = int((instance.rooms.price // 100 * 40))
                instance.price = int((instance.rooms.price * int(days)) + percent)
                print(instance.price)
                instance.save()
            # не один день и 3 человека!
            elif int(days) != int(0) and instance.guest_count > int(2):
                percent = int((instance.rooms.price) // 100 * 70)
                instance.price = int((instance.rooms.price * int(days)) + percent)
                instance.save()
        else:
            days = (instance.leave_date - instance.visit_date).days
            if int(days) == int(0):
                instance.price = instance.rooms.price
                instance.save()
            else:
                instance.price = instance.rooms.price * int(days)
                instance.save()

    elif not created:
        days = (instance.leave_date - instance.visit_date).days
        ranee = (instance.price // instance.rooms.price)
        aprice = (instance.rooms.price) #10 000
        izmeneno = (days)
        old_price = instance.price - (aprice * ranee)
        pricc = (aprice * izmeneno) + old_price
        Registration.objects.filter(id=instance.pk).update(price=pricc)
        instance.rooms.room_bool = instance.room_bool
        instance.rooms.save()
