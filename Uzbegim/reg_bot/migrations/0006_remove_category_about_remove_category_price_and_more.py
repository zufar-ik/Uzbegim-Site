# Generated by Django 4.0.4 on 2022-06-02 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg_bot', '0005_remove_category_img_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='about',
        ),
        migrations.RemoveField(
            model_name='category',
            name='price',
        ),
        migrations.RemoveField(
            model_name='category',
            name='room_num',
        ),
        migrations.AddField(
            model_name='image',
            name='about',
            field=models.TextField(default=1, verbose_name='Подробности'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='price',
            field=models.IntegerField(default=1, verbose_name='Цена'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='room_num',
            field=models.IntegerField(default=1, verbose_name='Номер'),
            preserve_default=False,
        ),
    ]