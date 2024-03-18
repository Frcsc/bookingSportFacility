from django.contrib.auth import get_user_model
from django.urls import reverse
from factory import fuzzy
from rest_framework import status
from rest_framework.test import APITestCase

from customers.tests.factories import CustomerProfileFactory
from users.tests.factories import TwoFactorAuthenticationFactory, UserFactory

User = get_user_model()


class CustomerRequestNewVerficationCodeTests(APITestCase):
    def setUp(self):
        super().setUp()
        self.url = reverse("customers:request-otp")
        self.email = fuzzy.FuzzyText(suffix="@example.com").fuzz()
        self.user = UserFactory(email=self.email)
        self.two_fa = TwoFactorAuthenticationFactory(user=self.user)
        self.customer = CustomerProfileFactory(user=self.user)

    def test_request_new_otp_with_valid_email(self):
        data = {"email": self.email}
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_request_new_otp_with_incorrect_email(self):
        data = {"email": "tribe@gmail.com"}
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
