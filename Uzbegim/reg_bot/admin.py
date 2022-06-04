from django.contrib import admin
from .models import User, Category, Image


class User_inline(admin.StackedInline):
    model = User


class User_db(admin.ModelAdmin):
    list_display = ('tg_id', 'nickname', 'username','lang')
    list_filter = ('username',)


class Room_inline(admin.StackedInline):
    model = Image


@admin.register(Category)  # model основного класса
class ImageAdmin(admin.ModelAdmin):
    inlines = [Room_inline]
    class Meta:
        model = Category

    list_display = ('name', 'room_num', 'price')
    list_filter = ('name',)

admin.site.register(User, User_db)
