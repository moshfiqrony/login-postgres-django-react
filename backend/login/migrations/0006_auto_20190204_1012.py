# Generated by Django 2.1.5 on 2019-02-04 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_userinfo2'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserInfo2',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='email2',
        ),
    ]