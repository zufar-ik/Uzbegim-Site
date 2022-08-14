from django.db import models

import django.utils.timezone
from django.db import models

from django.contrib.auth.models import User, UserManager
import datetime

year = datetime.datetime.now().year
month = datetime.datetime.now().month
day = datetime.datetime.now().day


class Rooms(models.Model):
    objects = None
    room_num = models.IntegerField(verbose_name='Комната')
    room_bool = models.BooleanField(default=True, verbose_name='Релевантность')
    category = models.CharField(max_length=150, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена (сум)', null=True)

    def __str__(self):
        return f'{self.room_num}'

    class Meta:
        verbose_name = 'Комнату'
        verbose_name_plural = 'Комнаты'


class Registration(models.Model):
    type = [
        ('Site', 'Сайт'),
        ('Bot', 'Бот'),
        ('Reseption', 'Ресепшен')
    ]
    objects = None
    rooms = models.ForeignKey(Rooms, on_delete=models.CASCADE, verbose_name='Номер',
                              help_text='Номер в который хотите заселить гостя!',
                              limit_choices_to={'room_bool': True}, related_name='reg'
                              )
    first_name = models.CharField(max_length=150, verbose_name='Имя')
    last_name = models.CharField(max_length=150, verbose_name='Фамилия')
    admin = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Администратор', related_name='admins')
    pasport_serial_num = models.CharField(max_length=100, verbose_name='Серия паспорта', help_text='*AB-0123456')
    tel_num = models.CharField(max_length=12, verbose_name='Номер телефона')
    img = models.FileField(verbose_name='Фото документа', help_text='Загружайте файл в формате .pdf',
                           upload_to='Паспорт Клиентов')
    visit_date = models.DateField(
        default=django.utils.timezone.localdate, verbose_name='Дата прибытия')
    leave_date = models.DateField(blank=True, null=True, verbose_name='Дата отбытия', default='После ухода!')
    guest_count = models.IntegerField(default=1, verbose_name='Кол-во людей')
    room_bool = models.BooleanField(default=False, verbose_name='Релевантность',
                                    help_text='При бронирование отключите галочку')
    price = models.IntegerField(verbose_name='Цена (сум)', null=True)
    pay_type = models.CharField(max_length=15, choices=type, verbose_name='Платеж произведен')

    def __str__(self):
        return f'{self.rooms},{self.last_name},{self.first_name},{self.room_bool},{self.admin}'

    class Meta:
        verbose_name = 'Номер'
        verbose_name_plural = 'Регистрация'
