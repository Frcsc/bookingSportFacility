from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from users.models import TwoFactorAuthentication

User = get_user_model()


class CustomUserAdmin(UserAdmin):
    list_display = ("email", "is_verified", "is_staff")
    list_filter = ("is_staff",)
    search_fields = ("email",)
    ordering = ("email",)
    filter_horizontal = ()

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_verified", "is_staff")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )


admin.site.register(User, CustomUserAdmin)


class TwoFactorAuthenticationAdmin(admin.ModelAdmin):
    list_display = ['email', 'code']
    readonly_fields = ['user', 'created_at', 'updated_at']

    def email(self, obj):
        return obj.user.email


admin.site.register(TwoFactorAuthentication, TwoFactorAuthenticationAdmin)
