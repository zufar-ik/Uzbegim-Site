from django.contrib import admin

from .models import UserReg, UserImg, UserRoom


class PostImageAdmin(admin.StackedInline):
    model = UserReg

class PageAdmin(admin.ModelAdmin):

    list_display = ('room_category', 'first_name', 'last_name', 'visit_date','tel_num')
    list_filter = ('first_name',)

admin.site.register(UserReg, PageAdmin)

class Room_inline(admin.StackedInline):
    model = UserImg


@admin.register(UserRoom)  # model основного класса
class ImageAdmin(admin.ModelAdmin):
    inlines = [Room_inline]
    class Meta:
        model = UserRoom

    list_display = ('name', 'room_num', 'price')
    list_filter = ('name',)
