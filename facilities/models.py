from django.db import models

from kansala_sports.mixin import BaseModel


class CourtBase(BaseModel):
    name = models.CharField(max_length=128)
    is_available = models.BooleanField(default=True)
    logo = models.ImageField(null=True, blank=True)
    address = models.CharField(max_length=512)
    person_in_charge = models.ForeignKey(
        'operations.OperationProfile', on_delete=models.SET_NULL, null=True
    )
    booking_cost_per_hour = models.DecimalField(max_digits=22, decimal_places=2)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class FutsalCourt(CourtBase):
    pass


class TennisCourt(CourtBase):
    pass


class BadmintonCourt(CourtBase):
    pass
