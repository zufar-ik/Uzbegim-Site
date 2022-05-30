import requests
from rest_framework import serializers
from .models import Registration


class RegSerializer(serializers.ModelSerializer):
    admin = serializers.SlugRelatedField(slug_field='username', read_only=True)
    class Meta:
        model = Registration
        fields = [
            'id', 'rooms', 'first_name', 'last_name','admin', 'pasport_serial_num', 'birth_date', 'img',
            'visit_date',
            'leave_date', 'guest_count', 'room_bool']


class RegUpdate(serializers.ModelSerializer):
    class Meta:
        read_only_fields = ['rooms']
        fields = ('id', 'leave_date', 'room_bool')
        model = Registration


# class VoteSerializer(serializers.ModelSerializer):
#     choice = serializers.SlugRelatedField(slug_field='choice_text', read_only=True)
#     poll = serializers.SlugRelatedField(slug_field='question', read_only=True)
#     voted_by = serializers.SlugRelatedField(slug_field='username', read_only=True)
#
#     class Meta:
#         model = Vote
#         fields = '__all__'