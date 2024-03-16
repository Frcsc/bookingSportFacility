from unittest.mock import patch

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from customers.models import CustomerProfile
from users.models import TwoFactorAuthentication

User = get_user_model()


class CustomerRegisterTests(APITestCase):
    def test_create_user(self):
        url = reverse("customers:register")
        data = {
            "email": "sedia.jaiteh@ymail.com",
            "name": "sedia",
            "password": "1442Dddn@",
        }
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)

        user = User.objects.get(email='sedia.jaiteh@ymail.com')
        self.assertEqual(user.is_verified, False)


class CustomerTwoFATests(APITestCase):
    def setUp(self) -> None:
        super().setUp()
        self.user = User.objects.create_user(
            email="sedia.jaiteh@ymail.com", password='1442Dddn@'
        )
        self.customer = CustomerProfile.objects.create(user=self.user, name="sedia")
        two_fa = TwoFactorAuthentication(user=self.user)
        two_fa.set_new_code()
        two_fa.save()
        self.two_fa = two_fa

    @patch('users.models.User.objects.get')
    @patch('users.models.TwoFactorAuthentication.objects.get')
    def test_two_fa_verification(self, mock_two_fa_get, mock_user_get):
        url = reverse("customers:two-factor-verification")

        mock_user_get.return_value = self.user
        mock_two_fa_get.return_value = self.two_fa

        data = {
            "email": self.customer.user.email,
            "code": self.two_fa.code,
        }

        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.user.is_verified, True)
