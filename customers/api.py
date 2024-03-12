from django.contrib.auth import get_user_model
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from customers.serializers import (
    CustomerProfileSerializer,
    CustomerRequestNewVerficationCodeSerializer,
    CustomerTwoFactorVerificationSerializer,
    RegisterCustomerSerializer,
)
from users.models import TwoFactorAuthentication
from users.permissions import AllowAnyPermission, CustomerPermission
from users.throttle import CustomAnonThrottle

User = get_user_model()


class CustomerRegisterationAPIView(AllowAnyPermission, APIView):
    def post(self, request, *args, **kwargs):
        serializer = RegisterCustomerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        two_fa = TwoFactorAuthentication(user=user)
        two_fa.set_new_code()
        two_fa.save()
        two_fa.send_two_factor_code_email(user.customer.name)

        return Response(
            'Please proceed to verify your email', status=status.HTTP_201_CREATED
        )


class CustomerTwoFactorVerificationAPIView(AllowAnyPermission, APIView):
    def post(self, request, *args, **kwargs):
        serializer = CustomerTwoFactorVerificationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        code = serializer.validated_data['code']
        email = serializer.validated_data['email']

        user = User.objects.get(email=email)
        two_fa = TwoFactorAuthentication.objects.get(user=user)

        if not two_fa.code == code:
            return Response('Invalid Code', status=status.HTTP_400_BAD_REQUEST)

        if two_fa.code_has_expired(code) is False:
            user.is_verified = True
            user.save()
            return Response('Verification successfull', status=status.HTTP_200_OK)
        return Response('Code has expired', status=status.HTTP_400_BAD_REQUEST)


class CustomerRequestNewVerficationCodeAPIView(
    AllowAnyPermission, CustomAnonThrottle, APIView
):
    def post(self, request, *args, **kwargs):
        serializer = CustomerRequestNewVerficationCodeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']

        user = User.objects.get(email=email)
        two_fa = TwoFactorAuthentication.objects.get(user=user)
        two_fa.set_new_code()
        two_fa.save()
        two_fa.send_two_factor_code_email(user.customer.name)

        return Response(
            'Please proceed to verify your email', status=status.HTTP_200_OK
        )


class CustomerProfileAPIView(CustomerPermission, generics.RetrieveAPIView):
    serializer_class = CustomerProfileSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.request.user.customerprofile
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
