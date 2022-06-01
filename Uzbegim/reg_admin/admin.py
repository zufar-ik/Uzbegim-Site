from django.contrib import admin

from .models import Registration, Rooms


class PostImageAdmin(admin.StackedInline):
    model = Registration


@admin.register(Rooms)  # model основного класса
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    class Meta:
        model = Rooms
    list_display = ('room_num', 'category', 'room_bool', 'price')
    list_filter = ('category',)

class PageAdmin(admin.ModelAdmin):
    def get_form(self, request, *args, **kwargs):
        form = super(PageAdmin, self).get_form(request, *args, **kwargs)
        form.base_fields['admin'].initial = request.user
        return form

    list_display = ('rooms', 'first_name', 'last_name', 'visit_date', 'leave_date', 'admin', 'room_bool', 'price')
    list_filter = ('rooms',)

admin.site.register(Registration, PageAdmin)
