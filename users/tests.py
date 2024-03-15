from django.test import TestCase

from users.models import User


class AnimalTestCase(TestCase):
    def setUp(self):
        User.objects.create(email="sedia.jaiteh@ymail.com")

    def test_animals_can_speak(self):
        user = User.objects.get(email="sedia.jaiteh@ymail.com")
        self.assertEqual(user.is_verified, False)
