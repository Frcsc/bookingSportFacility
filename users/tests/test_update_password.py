from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.urls import reverse
from factory import fuzzy
from rest_framework import status
from rest_framework.test import APITestCase

from users.tests.factories import UserInstance

User = get_user_model()
password_reset_token = PasswordResetTokenGenerator()


class InitiateResetPasswordTest(APITestCase):
    def setUp(self):
        super().setUp()
        self.email = fuzzy.FuzzyText(suffix="@example.com").fuzz()
        self.password = '@#$@6y2yt223'
        self.user = UserInstance(self.email, self.password)
        self.url = reverse("users:password-reset")
        self.token = password_reset_token.make_token(self.user)

    def test_invalid_token(self):
        data = {
            "email": self.email,
            "token": "jdjrfnrir1234jhjici",
            "password": self.password,
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_password_pattern(self):
        data = {
            "email": self.email,
            "token": self.token,
            "password": "9933",
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_email(self):
        data = {
            "email": "wrong_email@gmail.com",
            "token": self.token,
            "password": self.password,
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_correct_data(self):
        data = {
            "email": self.email,
            "token": self.token,
            "password": self.password,
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
