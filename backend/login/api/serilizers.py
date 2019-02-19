from rest_framework import serializers

from ..models import UserDetails
from ..models import UserInfo

class UserLoginInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ('id','username', 'password', 'email')

class UserDetailsfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = ('id','firstname', 'lastname', 'uid')
