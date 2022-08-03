from django.db.models.signals import post_save
from django.dispatch import receiver
import requests
from .models import UserReg

from environs import Env

# Используем библиотеку environs
env = Env()
env.read_env()
ADMINS = (env.list('ADMIN_BOT'))  # Список админов

@receiver(post_save, sender=UserReg)
def create_profile(sender, instance, created, **kwargs):
    if created:
        token = '5419456477:AAH4XGE9O-90vgiDHVTiV2Kmq8JWXiXFRNw'
        URL = 'https://api.telegram.org/bot' + token + '/sendMessage'
        for chat_id in ADMINS:
            try:
                # print(admin)
                data = {'chat_id': chat_id, 'text': "Забронирован один номер через сайт User\n\n"
                                                    "Посмотрите по ссылке http://127.0.0.1:8000/admin/reg_user/userreg/\n\n"
                                                    "Нажмите /start чтобы вывести меню администратора"}
                requests.post(URL, data=data)
            except Exception:
                pass


