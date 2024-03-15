from rest_framework.response import Response
from rest_framework.views import APIView

from bookings.models import BadmintonCourtBooking
from bookings.serializers import BadmintonCourtBookingSerializer
from users.permissions import AllowAnyPermission


class BadmintonCourtBookingList(AllowAnyPermission, APIView):
    def get(self, request, *args, **kwargs):
        day = kwargs.get('day')
        bookings = BadmintonCourtBooking.objects.filter(day=day)
        serializer = BadmintonCourtBookingSerializer(bookings, many=True)

        return Response(serializer.data)


# Book a badmington court
