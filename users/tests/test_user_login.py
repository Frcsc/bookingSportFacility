from django.contrib.auth import get_user_model
from django.urls import reverse
from factory import fuzzy
from rest_framework import status
from rest_framework.test import APITestCase

from users.tests.factories import UserInstance

User = get_user_model()


class UserLoginTest(APITestCase):
    def setUp(self):
        super().setUp()
        self.email = fuzzy.FuzzyText(suffix="@example.com").fuzz()
        self.password = '@#$@6y2yt223'
        self.user = UserInstance(self.email, self.password)
        self.url = reverse("users:login")

    def test_invalid_password_user_login(self):
        data = {"email": self.email, "password": 'yshgbs@@dhs1'}
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_email_user_login(self):
        data = {"email": 'dummy@gmail.com', "password": self.password}
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_password__pattern_user_login(self):
        data = {"email": 'dummy@gmail.com', "password": 555555}
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_unverified_user_login(self):
        data = {"email": self.email, "password": self.password}
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_verified_user_login(self):
        self.user.is_verified = True
        self.user.save()
        data = {"email": self.email, "password": self.password}
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
