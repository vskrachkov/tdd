import factory

from . import models


class ItemFactory(factory.DjangoModelFactory):
    """"""
    text = factory.Faker('sentence', nb_words=5)

    class Meta:
        model = models.Item
