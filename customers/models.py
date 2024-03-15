from django.db import models

from kansala_sports.mixin import BaseModel


class CustomerProfile(BaseModel):
    user = models.OneToOneField('users.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name
