from django.db import models

from django.contrib.auth.models import User
import datetime
year = datetime.datetime.now().year
month = datetime.datetime.now().month
day = datetime.datetime.now().day


class Rooms(models.Model):
    objects = None
    room_num = models.IntegerField(verbose_name='Комната')
    room_bool = models.BooleanField(default=True,verbose_name='Релевантность')
    category = models.CharField(max_length=150,verbose_name='Категория')
    price = models.CharField(max_length=105,verbose_name='Цена (сум)')
    def __str__(self):
        return f'{self.room_num}'

    class Meta:
        verbose_name = 'Комнату'
        verbose_name_plural = 'Комнаты'

class Registration(models.Model):
    objects = None
    rooms = models.ForeignKey(Rooms, on_delete=models.CASCADE,verbose_name='Номер',help_text='Номер в который хотите заселить гостя!',limit_choices_to = {'room_bool': True},)
    first_name = models.CharField(max_length=150,verbose_name='Имя')
    last_name = models.CharField(max_length=150,verbose_name='Фамилия')
    admin = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='Администратор')
    pasport_serial_num = models.CharField(max_length=100,verbose_name='Серия паспорта',help_text='*AB-0123456')
    birth_date = models.DateField(verbose_name='Дата рождения')
    img = models.FileField(verbose_name='Фото документа',help_text='Загружайте файл в формате .pdf')
    visit_date = models.DateTimeField(
        default=datetime.datetime(year=year, month=month, day=day, hour=datetime.datetime.now().hour,
                                  minute=datetime.datetime.now().minute, second=00,),verbose_name='Дата прибытия')
    leave_date = models.DateTimeField(
        default=datetime.datetime(year=year, month=month, day=day + 1, hour=12, minute=00, second=00),verbose_name='Дата отбытия')
    guest_count = models.IntegerField(default=1,verbose_name='Кол-во людей')
    room_bool = models.BooleanField(default=False,verbose_name='Релевантность',help_text='При бронирование отключите галочку')
    price = models.CharField(max_length=105,default='Появится после сохранения!',verbose_name='Цена (сум)')
    def __str__(self):
        return f'{self.rooms},{self.last_name},{self.first_name},{self.room_bool}'

    class Meta:
        verbose_name = 'Номер'
        verbose_name_plural = 'Регистрация'
