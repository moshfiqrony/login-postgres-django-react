from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from ..models import UserInfo
from .serilizers import UserLoginInfoSerializer

class UserInfoViewById(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserLoginInfoSerializer

    def retrieve(self, request, pk=None):
        queryset = UserInfo.objects.all()
        user = get_object_or_404(queryset, username=pk)
        serializer = UserLoginInfoSerializer(user)
        return Response(serializer.data)