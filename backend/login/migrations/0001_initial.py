# Generated by Django 2.1.5 on 2019-02-04 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=80, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=140, unique=True)),
            ],
        ),
    ]
