# Generated by Django 3.2.13 on 2022-05-27 08:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg_admin', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='price',
        ),
        migrations.AlterField(
            model_name='registration',
            name='leave_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 28, 12, 0), verbose_name='Дата отбытия'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='visit_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 27, 13, 8), verbose_name='Дата прибытия'),
        ),
    ]