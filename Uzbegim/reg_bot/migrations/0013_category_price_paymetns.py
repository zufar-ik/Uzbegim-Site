# Generated by Django 4.0.4 on 2022-06-03 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg_bot', '0012_category_bron_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='price_paymetns',
            field=models.IntegerField(default=1, verbose_name='Цена для платежа'),
            preserve_default=False,
        ),
    ]
