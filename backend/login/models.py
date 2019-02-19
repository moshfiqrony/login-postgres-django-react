from django.db import models

class UserInfo(models.Model):
    username = models.CharField(max_length=80, unique=True)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=140, unique=True)

class UserDetails(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    uid = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
