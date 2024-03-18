import factory
from factory import fuzzy


class CustomerProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'customers.CustomerProfile'

    name = fuzzy.FuzzyText()
    user = factory.SubFactory("users.tests.factories.UserFactory")
