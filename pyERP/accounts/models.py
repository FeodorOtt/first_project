from django.contrib import auth
from django.db import models
from django.utils import timezone
from funds.models import Client


class UsersInfo(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE,)
    client = models.ForeignKey('funds.Client', on_delete=models.SET_NULL, null=True)
    bria_name = models.CharField(max_length=100, null=True)
    status_id = models.SmallIntegerField()
