from django.contrib.auth import get_user_model
from django.urls import reverse
from factory import fuzzy
from rest_framework import status
from rest_framework.test import APITestCase

from customers.tests.factories import CustomerProfileFactory
from users.tests.factories import AuthTokenFactory, UserFactory

User = get_user_model()


class CustomerAPITestCase(APITestCase):
    def setUp(self):
        super().setUp()
        self.email = fuzzy.FuzzyText(suffix="@example.com").fuzz()
        self.user = UserFactory(email=self.email, is_verified=True)
        self.customer = CustomerProfileFactory(user=self.user)
        self.instance, self.token = AuthTokenFactory(user=self.user)
        self.access_token = "Token " + self.token
        self.url = reverse("customers:profile")


class CustomerProfileTests(CustomerAPITestCase):
    def test_get_customer_profile_with_correct_data(self):
        headers = {'HTTP_AUTHORIZATION': self.access_token}
        response = self.client.get(self.url, format="json", **headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_customer_profile_with_invalid_email(self):
        headers = {'HTTP_AUTHORIZATION': 'hdyHGSTHjjcdudhdnm23384Bb'}
        response = self.client.get(self.url, format="json", **headers)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
