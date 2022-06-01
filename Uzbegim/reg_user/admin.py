from django.contrib import admin

from .models import UserReg

class PostImageAdmin(admin.StackedInline):
    model = UserReg

class PageAdmin(admin.ModelAdmin):

    list_display = ('room_category', 'first_name', 'last_name', 'visit_date','tel_num')
    list_filter = ('first_name',)

admin.site.register(UserReg, PageAdmin)
