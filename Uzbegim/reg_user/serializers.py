from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ModelSerializer, RelatedField
from .models import UserReg, UserRoom, UserImg


class User(ModelSerializer):
    class Meta:
        model = UserReg
        fields = '__all__'

class AllRooms(ModelSerializer):
    class Meta:
        model = UserRoom
        fields = '__all__'

class UserImgSer(ModelSerializer):
    class Meta:
        model = UserImg
        fields = '__all__'


class UserRoomSer(ModelSerializer):
    images = UserImgSer(source='userimg_set', many=True)

    class Meta:
        model = UserRoom
        fields = [
            'id','name', 'room_num', 'about', 'price',
            'img360', 'images',
        ]
