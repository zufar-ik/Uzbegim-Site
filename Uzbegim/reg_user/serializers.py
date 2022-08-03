from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ModelSerializer
from .models import UserReg, UserRoom, UserImg


class User(ModelSerializer):
    class Meta:
        model = UserReg
        fields = '__all__'


class UserRoomSer(ModelSerializer):
    class Meta:
        model = UserRoom
        fields = '__all__'