from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    created_at = models.DateTimeField(default=timezone.localtime)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# class FacilitiesBaseModel(models.Model):
#     name = models.CharField(max_length=128)
#     is_available = models.BooleanField(default=True)
#     logo = models.ImageField()
#     address = models.CharField(max_length=512)
#     person_in_charge = models.ForeignKey(
#         'users.OperationUser', on_delete=models.SET_NULL, null=True
#     )

#     class Meta:
#         abstract = True

#     def __str__(self):
#         return self.name
