from django.contrib import admin

from bookings.models import BadmintonCourtBooking, Booking


class BadmintonCourtBookingAdmin(admin.ModelAdmin):
    list_display = ["id", "customer_name", "customer_email", "time"]

    def customer_name(self, obj):
        return obj.booking.customer.name

    def customer_email(self, obj):
        return obj.booking.customer.user.email


admin.site.register(BadmintonCourtBooking, BadmintonCourtBookingAdmin)


class BookingAdmin(admin.ModelAdmin):
    list_display = ["id", "customer_name", "customer_email"]

    def customer_name(self, obj):
        return obj.customer.name

    def customer_email(self, obj):
        return obj.customer.user.email


admin.site.register(Booking, BookingAdmin)
