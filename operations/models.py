from django.db import models

from kansala_sports.mixin import BaseModel


class OperationProfile(BaseModel):
    name = models.CharField(max_length=128)
    user = models.OneToOneField('users.User', on_delete=models.CASCADE)
