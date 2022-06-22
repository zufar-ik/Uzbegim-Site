from rest_framework import serializers

from .models import Registration


class RegSerializer(serializers.ModelSerializer):
    admin = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Registration
        exclude = ['price', 'visit_date']

class RegViews(serializers.ModelSerializer):
    admin = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Registration
        fields = "__all__"

class RegUpdate(serializers.ModelSerializer):
    rooms = serializers.SlugRelatedField(slug_field='room_num', read_only=True)
    admin = serializers.SlugRelatedField(slug_field='username', read_only=True)
    visit_date = serializers.PrimaryKeyRelatedField(read_only=True)
    first_name = serializers.PrimaryKeyRelatedField(read_only=True)
    last_name = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Registration
        fields = ['rooms', 'first_name', 'last_name', 'visit_date', 'leave_date', 'room_bool', 'admin']

class RegDeteil(serializers.ModelSerializer):
    rooms = serializers.SlugRelatedField(slug_field='room_num', read_only=True)
    admin = serializers.SlugRelatedField(slug_field='username', read_only=True)
    class Meta:
        model = Registration
        fields = "__all__"
