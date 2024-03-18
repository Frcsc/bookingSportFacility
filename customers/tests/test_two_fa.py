from django.contrib.auth import get_user_model
from django.urls import reverse
from factory import fuzzy
from rest_framework import status
from rest_framework.test import APITestCase

from users.tests.factories import TwoFactorAuthenticationFactory, UserFactory

User = get_user_model()


class CustomerAuthenticateTwoFaTests(APITestCase):
    def setUp(self):
        super().setUp()
        self.url = reverse("customers:two-factor-verification")
        self.email = fuzzy.FuzzyText(suffix="@example.com").fuzz()
        self.user = UserFactory(email=self.email)
        self.two_fa = TwoFactorAuthenticationFactory(user=self.user)

    def test_verify_correct_otp(self):
        data = {"email": self.email, "code": self.two_fa.code}
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_verify_expired_otp(self):
        data = {"email": self.email, "code": 245251}
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_verify_invalid_email_otp(self):
        data = {"email": 'test@gmail.com', "code": self.two_fa.code}
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)