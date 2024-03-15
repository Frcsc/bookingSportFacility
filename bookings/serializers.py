from rest_framework import serializers

from bookings.models import BadmintonCourtBooking, Booking
from facilities.models import BadmintonCourt
from operations.models import OperationProfile


class BadmintonCourtBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BadmintonCourtBooking
        fields = ['id', 'day', 'time', 'booking', 'court']

    class BookingSerializer(serializers.ModelSerializer):
        class Meta:
            model = Booking
            fields = ['id', 'created_at']

    class CourtSerializer(serializers.ModelSerializer):
        class Meta:
            model = BadmintonCourt
            exclude = ['updated_at', 'created_at']

        class OperationProfileSerializer(serializers.ModelSerializer):
            class Meta:
                model = OperationProfile
                exclude = ['updated_at', 'created_at', 'user']

        person_in_charge = OperationProfileSerializer()

    booking = BookingSerializer()
    court = CourtSerializer()
