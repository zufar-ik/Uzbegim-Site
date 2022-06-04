from django.db import models


class User(models.Model):
    tg_id = models.BigIntegerField(unique=True)
    nickname = models.CharField(max_length=250, null=True, verbose_name='Имя', blank=True)
    username = models.CharField(max_length=250, null=True, verbose_name='Имя пользователя', blank=True)
    lang = models.CharField(max_length=10,default='ru',verbose_name='Язык',null=True)

    class Meta:
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'


class Category(models.Model):
    categoty = [
        ('President Lux', 'President Lux'),
        ('Lux', 'Lux'),
        ('Double', 'Double'),
        ('Standard', 'Standard'),
    ]
    name = models.CharField(max_length=150, choices=categoty, verbose_name='Категория')
    slug = models.SlugField(verbose_name='Слаг')
    bron_slug = models.SlugField(verbose_name='Cлаг для заказа',null=True)
    room_num = models.CharField(verbose_name='Номер', max_length=250)
    about = models.TextField(verbose_name='Подробности')
    about_payments = models.TextField(verbose_name='Подробности во время платежа',default='После успешной оплаты средств вам предаставят чек (QR-CODE)\n\n'
                                                                                          'Сохраните ее для подтверждения во время прихода в "Hotel Uzbegim"')
    price = models.CharField(verbose_name='Цена',max_length=150)
    price_paymetns = models.IntegerField(verbose_name='Цена для платежа')
    logo = models.URLField('Логотип')

    class Meta:
        verbose_name = 'Категорий'
        verbose_name_plural = 'Категория'


class Image(models.Model):
    name = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='img1')
    img = models.URLField(verbose_name='Фотография')



