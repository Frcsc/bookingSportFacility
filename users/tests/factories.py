# import datetime
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

    # digest = fuzzy.FuzzyText(length=128).fuzz()
    # token_key = fuzzy.FuzzyText(length=128).fuzz()
    user = factory.SubFactory(UserFactory)
    # created = fuzzy.FuzzyDateTime(datetime.datetime(2021, 1, 1, tzinfo=datetime.timezone.utc)).fuzz()
    # expiry  = fuzzy.FuzzyDateTime(start_dt=created + datetime.timedelta(hours=1)).fuzz()
