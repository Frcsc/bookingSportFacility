from rest_framework.test import APITestCase

from django.contrib.auth import get_user_model
from django.urls import reverse
from factory import fuzzy
from rest_framework import status
from rest_framework.test import APITestCase

from users.tests.factories import TwoFactorAuthenticationFactory, UserFactory

User = get_user_model()

class UserLoginTest(APITestCase):
    def setUp(self):
        super().setUp()
        self.email = fuzzy.FuzzyText(suffix="@example.com").fuzz()
        self.password = '@#$@6y2yt223'
        self.user = UserFactory(email=self.email, password=self.password)
        self.url = reverse("users:login")

    def test_user_login(self):
        data = {
            "email": self.email,
            "password": self.password
        }
        response = self.client.post(self.url, data=data, format="json")
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
