from django.db import models


class User(models.Model):
    name = models.CharField(max_length=150)
    username = models.CharField(max_length=150)
    class Meta:
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'


class Reg_nomer(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    birth_date = models.DateField()
    visit_date = models.DateTimeField()
    leave_date = models.DateTimeField()
    guest_count = models.IntegerField()
    room_num = models.IntegerField()
    price = models.IntegerField()


