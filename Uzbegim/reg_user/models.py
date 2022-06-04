from django.db import models

import django.utils.timezone

from reg_admin.models import Rooms


class UserReg(models.Model):
    objects = None
    rooms = models.ForeignKey(Rooms, on_delete=models.CASCADE, verbose_name='Номер',
                              help_text='Номер в который хотите заселить гостя!', related_name='user'
                              )
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
        verbose_name = 'Номер (Reg)'
        verbose_name_plural = 'Номера (Reg)'


class UserRoom(models.Model):
    categoty = [
        ('President Lux', 'President Lux'),
        ('Lux', 'Lux'),
        ('Double', 'Double'),
        ('Standard', 'Standard'),
    ]
    name = models.CharField(max_length=150, choices=categoty, verbose_name='Категория')
    room_num = models.CharField(max_length=150)
    about = models.TextField(verbose_name='Подробности')
    price = models.IntegerField(verbose_name='Цена')

    class Meta:
        verbose_name = 'Номер (About)'
        verbose_name_plural = 'Номера (About)'


class UserImg(models.Model):
    name = models.ForeignKey(UserRoom, on_delete=models.CASCADE, verbose_name='img2')
    img = models.FileField(upload_to='User img', verbose_name='Фотография')

    class Meta:
        verbose_name = 'Фотографию'
        verbose_name_plural = 'Фотографии'
