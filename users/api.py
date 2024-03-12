from knox.models import AuthToken
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from users.permissions import AllowAnyPermission
from users.serializers import LoginSerializer


class LoginAPIView(AllowAnyPermission, APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data

        if not user.is_verified:
            return Response(
                'Please verify your email', status=status.HTTP_401_UNAUTHORIZED
            )

        instance, token = AuthToken.objects.create(user)

        return Response(
            {'token': token, 'expiry': instance.expiry}, status=status.HTTP_200_OK
        )


class ResetPassword(AllowAnyPermission, APIView):
    pass