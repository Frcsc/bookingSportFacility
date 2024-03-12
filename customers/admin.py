from django.contrib import admin

from customers.models import CustomerProfile


class CustomerProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']

    def email(self, obj):
        return obj.user.email


admin.site.register(CustomerProfile, CustomerProfileAdmin)
