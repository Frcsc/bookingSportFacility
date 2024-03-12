from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.shortcuts import get_object_or_404
from knox.models import AuthToken
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from users.permissions import AllowAnyPermission
from users.serializers import (
    LoginSerializer,
    UserRestPasswordInitiationSerializer,
    UserUpdatePasswordSerializer,
)

User = get_user_model()
password_reset_token = PasswordResetTokenGenerator()


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


class ResetPasswordAPIView(AllowAnyPermission, APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserRestPasswordInitiationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']

        user = get_object_or_404(User, email=email)

        user.send_reset_password_link()
        return Response(
            'We have sent you a password reset email, please check your inbox',
            status=status.HTTP_200_OK,
        )


class UserUpdatePasswordAPIView(AllowAnyPermission, APIView):
    def post(self, request, *args, **kwargs):

        serializer = UserUpdatePasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        token = serializer.validated_data['token']
        password = serializer.validated_data['password']

        user = get_object_or_404(User, email=email)

        if password_reset_token.check_token(user, token):
            user.set_password(password)
            user.save()
            return Response('Password updated', status=status.HTTP_200_OK)
        return Response(
            'Invalid password update token', status=status.HTTP_400_BAD_REQUEST
        )
