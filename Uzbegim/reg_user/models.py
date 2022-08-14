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
    tel_num = models.BigIntegerField(verbose_name='Номер телефона')
    tel_num2 = models.BigIntegerField(verbose_name='Номер телефона (2)', null=True, blank=True)
    visit_date = models.DateField(
        default=django.utils.timezone.localdate, verbose_name='Дата прибытия')
    leave_date = models.DateField(blank=True, null=True, verbose_name='Дата отбытия')
    email = models.EmailField()
    guest_count = models.IntegerField(default=1, verbose_name='Кол-во людей')

    class Meta:
        verbose_name = 'Номер (Reg)'
        verbose_name_plural = 'Номера (Reg)'


class UserRoom(models.Model):
    objects = None
    categoty = [
        ('President Lux', 'President Lux'),
        ('Lux', 'Lux'),
        ('Double', 'Double'),
        ('Standard', 'Standard'),
    ]
    name = models.CharField(max_length=150, choices=categoty, verbose_name='Категория')
    room_num = models.CharField(max_length=150, verbose_name='Доступные номера для категории')
    about = models.TextField(verbose_name='Подробности')
    price = models.IntegerField(verbose_name='Цена')
    img360 = models.FileField(verbose_name='Фотография в 360',upload_to='Room .img/')

    class Meta:
        verbose_name = 'Номер (About)'
        verbose_name_plural = 'Номера (About)'

    def __str__(self):
        return f'{self.name}'


class UserImg(models.Model):
    objects = None
    name = models.ForeignKey(UserRoom, on_delete=models.CASCADE, related_name='userimg_set')
    img = models.FileField(upload_to='Room .img', verbose_name='Фотография')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Фотографию'
        verbose_name_plural = 'Фотографии'
