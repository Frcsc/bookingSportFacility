from django.urls import path, re_path
from knox import views as knox_views

from users import api

app_name = "customers"

urlpatterns = [
    path("login/", api.LoginAPIView.as_view(), name="login"),
    re_path(r"logout/", knox_views.LogoutView.as_view(), name="logout"),
    path(
        'password-reset-initiation/',
        api.InitiateResetPasswordAPIView.as_view(),
        name="password-reset-initiation",
    ),
    path(
        'password-reset/',
        api.UserUpdatePasswordAPIView.as_view(),
        name="password-reset",
    ),
]
