from rest_framework import permissions


class AllowAnyPermission:
    permission_classes = [permissions.AllowAny]


class BasePermission(permissions.IsAuthenticated):
    model = None

    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and user.is_verified and hasattr(user, self.model)


class CustomerPermissionMixin(BasePermission):
    model = 'customerprofile'


class CustomerPermission:
    permission_classes = [CustomerPermissionMixin]
