from django.contrib import admin

from operations.models import OperationProfile


class OperationProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']

    def email(self, obj):
        return obj.user.email


admin.site.register(OperationProfile, OperationProfileAdmin)
