from django.contrib import admin

from .models import Registration, Rooms

class PostImageAdmin(admin.StackedInline):
    model = Registration


@admin.register(Rooms) #model основного класса
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    class Meta:
        model = Rooms