from django.urls import path

from customers import api

app_name = "customers"

urlpatterns = [
    path("register/", api.CustomerRegisterationAPIView.as_view(), name="register"),
    path(
        "two-factor-verification/",
        api.CustomerTwoFactorVerificationAPIView.as_view(),
        name="two-factor-verification",
    ),
    path(
        "request-otp/",
        api.CustomerRequestNewVerficationCodeAPIView.as_view(),
        name="request-otp",
    ),
    path("profile/", api.CustomerProfileAPIView.as_view(), name="profile"),
]
