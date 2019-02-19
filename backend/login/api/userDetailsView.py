from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from ..models import UserDetails
from .serilizers import UserDetailsfoSerializer

class UserDetailsView(viewsets.ModelViewSet):
    queryset = UserDetails.objects.all()
    serializer_class = UserDetailsfoSerializer
