import secrets
import string

import factory
from factory import fuzzy
from knox.models import AuthToken


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'users.User'

    email = fuzzy.FuzzyText(suffix='@example.com').fuzz()


class TwoFactorAuthenticationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'users.TwoFactorAuthentication'

    user = factory.SubFactory(UserFactory)
    code = fuzzy.FuzzyText(
        chars=''.join(secrets.choice(string.digits) for i in range(6)), length=6
    ).fuzz()


class AuthTokenFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = AuthToken
    user = factory.SubFactory(UserFactory)
