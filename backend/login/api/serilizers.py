from rest_framework import serializers

from ..models import UserInfo

class UserLoginInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ('id', 'username', 'password', 'email')