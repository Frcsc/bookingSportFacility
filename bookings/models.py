from django.db import models
from django.utils import timezone

from bookings.enums import TIME_CHOICES
from kansala_sports.mixin import BaseModel


class Booking(BaseModel):
    customer = models.ForeignKey('customers.CustomerProfile', on_delete=models.CASCADE)

    def __str__(self):
        return self.customer.name


class CourtBooking(BaseModel):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    day = models.DateField(default=timezone.localtime)
    time = models.CharField(
        max_length=64, choices=TIME_CHOICES, default=TIME_CHOICES[0]
    )
    time_ordered = models.DateTimeField(default=timezone.localtime)

    def __str__(self):
        return self.booking.customer.name

    class Meta:
        abstract = True


class TennisCourtBooking(CourtBooking):
    court = models.ForeignKey('facilities.TennisCourt', on_delete=models.CASCADE)


class FutsalCourtBooking(CourtBooking):
    court = models.ForeignKey('facilities.FutsalCourt', on_delete=models.CASCADE)


class BadmintonCourtBooking(CourtBooking):
    court = models.ForeignKey('facilities.BadmintonCourt', on_delete=models.CASCADE)
