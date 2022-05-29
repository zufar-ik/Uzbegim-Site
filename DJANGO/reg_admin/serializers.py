from rest_framework import serializers
from .models import Registration


class RegSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'rooms', 'first_name', 'last_name', 'admin', 'pasport_serial_num', 'birth_date', 'img', 'visit_date', 'leave_date', 'guest_count', 'room_bool', 'price')
        model = Registration
