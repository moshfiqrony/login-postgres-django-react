from django.db import models

class UserInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=80, unique=True)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=120, unique=True)

