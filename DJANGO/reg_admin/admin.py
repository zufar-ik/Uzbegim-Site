from django.contrib import admin

from .models import Registration, Rooms


class PostImageAdmin(admin.StackedInline):
    model = Registration


@admin.register(Rooms)  # model основного класса
class PostAdmin(admin.ModelAdmin):

    class Meta:
        model = Rooms

    list_display = ('room_num', 'category', 'room_bool', 'price')
    list_filter = ('category',)


class PageAdmin(admin.ModelAdmin):
    list_display = ('rooms', 'first_name', 'last_name', 'visit_date', 'leave_date', 'admin', 'room_bool', 'price')
    list_filter = ('rooms',)
    raw_id_fields = ('admin',)

    readonly_fields = ('visit_date', 'price')
    admin.site.site_header = 'Uzbegim'

    def get_form(self, request, *args, **kwargs):
        form = super(PageAdmin, self).get_form(request, *args, **kwargs)
        form.base_fields['admin'].initial = request.user
        return form


admin.site.register(Registration, PageAdmin)
