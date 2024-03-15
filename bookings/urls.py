from django.urls import path

from bookings import api

app_name = "customers"

urlpatterns = [
    path(
        'available-badminton-court-slots/<str:day>/',
        api.BadmintonCourtBookingList.as_view(),
        name="available-badminton-court-slots",
    ),
]
