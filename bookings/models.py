from django.db import models

from kansala_sports.mixin import BaseModel


class Booking(BaseModel):
    customer = models.ForeignKey('customers.CustomerProfile', on_delete=models.CASCADE)


class CourtBooking(BaseModel):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    class Meta:
        abstract = True


class TennisCourtBooking(CourtBooking):
    court = models.ForeignKey('facilities.TennisCourt', on_delete=models.CASCADE)


class FutsalCourtBooking(CourtBooking):
    court = models.ForeignKey('facilities.FutsalCourt', on_delete=models.CASCADE)


class BadmintonCourtBooking(CourtBooking):
    court = models.ForeignKey('facilities.BadmintonCourt', on_delete=models.CASCADE)
