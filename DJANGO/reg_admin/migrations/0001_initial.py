# Generated by Django 4.0.4 on 2022-05-20 15:10

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_num', models.IntegerField()),
                ('room_bool', models.BooleanField(default=True)),
                ('category', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('pasport_serial_num', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
                ('img', models.FileField(upload_to='')),
                ('visit_date', models.DateTimeField(default=datetime.datetime(2022, 5, 20, 20, 10))),
                ('leave_date', models.DateTimeField(default=datetime.datetime(2022, 5, 21, 12, 0))),
                ('guest_count', models.IntegerField(default=1)),
                ('room_bool', models.BooleanField(default=False)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('rooms', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reg_admin.rooms')),
            ],
        ),
    ]
