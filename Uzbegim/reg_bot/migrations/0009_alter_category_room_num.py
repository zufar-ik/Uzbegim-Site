# Generated by Django 4.0.4 on 2022-06-02 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg_bot', '0008_remove_category_img_image_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='room_num',
            field=models.CharField(max_length=250, verbose_name='Номер'),
        ),
    ]
