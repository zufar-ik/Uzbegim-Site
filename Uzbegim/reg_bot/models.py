from django.db import models


class User(models.Model):
    tg_id = models.BigIntegerField(unique=True)
    nickname = models.CharField(max_length=250, null=True, verbose_name='Имя', blank=True)
    username = models.CharField(max_length=250, null=True, verbose_name='Имя пользователя', blank=True)
    lang = models.CharField(max_length=10, default='ru', verbose_name='Язык', null=True)

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
    bron_slug = models.SlugField(verbose_name='Cлаг для заказа', null=True)
    room_num = models.CharField(verbose_name='Номер', max_length=250)
    about_en = models.TextField(verbose_name='Подробности English', null=True)
    about_ru = models.TextField(verbose_name='Подробности на Русском', null=True)
    about_uz = models.TextField(verbose_name="Подробности O'zbekcha", null=True)
    about_payments_ru = models.TextField(verbose_name='Подробности во время платежа',
                                         default='После успешной оплаты средств вам предаставят чек (QR-CODE)\n\n'
                                                 'Сохраните ее для подтверждения во время прихода в "Hotel Uzbegim"')
    about_payments_en = models.TextField(verbose_name='Подробности во время платежа',
                                         default='After successful payment of funds, you will be provided with a receipt (QR-CODE)\n\n'
                                                 'Keep it for confirmation when you arrive at "Hotel Uzbegim"')
    about_payments_uz = models.TextField(verbose_name='Подробности во время платежа',
                                         default="Mablag'ni muvaffaqiyatli to'laganingizdan so'ng sizga chek (QR-CODE) beriladi\n\n"
                                                 "“Uzbegim” mehmonxonasiga kelganingizda uni tasdiqlash uchun saqlang")
    price_ru = models.CharField(verbose_name='Цена ₽', max_length=150)
    price_en = models.CharField(verbose_name='Цена $', max_length=150)
    price_uz = models.CharField(verbose_name='Цена', max_length=150)
    price_payments_uzs = models.IntegerField(verbose_name='Цена для платежа')
    price_payments_usd = models.IntegerField(verbose_name='Цена для платежа $')
    price_payments_rub = models.IntegerField(verbose_name='Цена для платежа ₽')
    logo = models.URLField('Логотип')

    class Meta:
        verbose_name = 'Категорий'
        verbose_name_plural = 'Категория'


class Image(models.Model):
    name = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='img1')
    img = models.URLField(verbose_name='Фотография')


class Successful_pay(models.Model):
    tg_id = models.BigIntegerField()
    room_category = models.CharField(max_length=150,null=True)
    price = models.BigIntegerField()
    currency = models.CharField(max_length=50)
    provider_payment_charge_id = models.TextField()
    qr_link = models.TextField()
    active = models.BooleanField(default=False)
    tel_num = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    name = models.TextField()
    visit_date = models.DateTimeField()
    leav_date = models.DateTimeField()
    day_count = models.IntegerField()
