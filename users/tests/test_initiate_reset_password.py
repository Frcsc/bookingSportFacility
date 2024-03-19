from django.contrib.auth import get_user_model
from django.urls import reverse
from factory import fuzzy
from rest_framework import status
from rest_framework.test import APITestCase

from users.tests.factories import UserInstance

User = get_user_model()


class InitiateResetPasswordTest(APITestCase):
    def setUp(self):
        super().setUp()
        self.email = fuzzy.FuzzyText(suffix="@example.com").fuzz()
        self.password = '@#$@6y2yt223'
        self.user = UserInstance(self.email, self.password)
        self.url = reverse("users:password-reset-initiation")

    def test_initiate_invalid_user_password(self):
        data = {"email": "test@mike.com"}
        response = self.client.post(self.url, data, format="json")
        self.assertNotEqual(response.status_code, status.HTTP_200_OK)

    def test_initiate_valid_user_password(self):
        data = {"email": self.email}
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
