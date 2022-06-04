from rest_framework.serializers import ModelSerializer
from .models import UserReg

class User(ModelSerializer):
    class Meta:
        model = UserReg
        fields = '__all__'