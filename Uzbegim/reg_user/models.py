from django.db import models

import django.utils.timezone

from reg_admin.models import Rooms


class UserReg(models.Model):
    objects = None
    Category = [
        ('standard', 'Standard'),
        ('double', 'Double'),
        ('lux', 'Lux'),
        ('president lux', 'President Lux'),
    ]
    room_category = models.CharField(max_length=50, choices=Category, verbose_name='Категория')
    first_name = models.CharField(max_length=150, verbose_name='Имя')
    last_name = models.CharField(max_length=150, verbose_name='Фамилия')
    birth_date = models.DateField(verbose_name='Дата рождения')
    tel_num = models.IntegerField(verbose_name='Номер телефона')
    tel_num2 = models.IntegerField(verbose_name='Номер телефона (2)', null=True, blank=True)
    visit_date = models.DateField(
        default=django.utils.timezone.localdate, verbose_name='Дата прибытия')
    leave_date = models.DateField(blank=True, null=True, verbose_name='Дата отбытия')
    email = models.EmailField()
    guest_count = models.IntegerField(default=1, verbose_name='Кол-во людей')

    class Meta:
        verbose_name = 'Номер пользователя'
        verbose_name_plural = 'Комнаты Пользователей'
