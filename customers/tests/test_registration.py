from django.contrib.auth import get_user_model
from django.urls import reverse
from factory import fuzzy
from rest_framework import status
from rest_framework.test import APITestCase

from customers.models import CustomerProfile
from users.models import TwoFactorAuthentication

User = get_user_model()


class CustomerRegisterTests(APITestCase):
    def setUp(self):
        super().setUp()
        self.url = reverse("customers:register")
        self.email = fuzzy.FuzzyText(suffix="@example.com").fuzz()
        self.name = fuzzy.FuzzyText(length=6).fuzz()
        self.password = '@#$@6y2yt223'

    def test_create_user(self):

        data = {
            "email": self.email,
            "name": self.name,
            "password": self.password,
        }

        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        user = User.objects.get(email=self.email)
        customer = CustomerProfile.objects.get(user__email=self.email)
        two_fa = TwoFactorAuthentication.objects.get(user__email=self.email)

        self.assertEqual(customer.user, user)

        self.assertEqual(two_fa.user, user)

        self.assertEqual(user.is_verified, False)

    def test_invalid_password_pattern(self):
        data = {
            "email": self.email,
            "name": self.name,
            "password": 'hello',
        }

        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_email_pattern(self):
        data = {
            "email": 'moha.gmail.com',
            "name": self.name,
            "password": self.password,
        }

        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_name_in_payload(self):
        data = {
            "email": self.email,
            "name": "",
            "password": self.password,
        }

        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
