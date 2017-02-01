import factory

from . import models


class ListFactory(factory.DjangoModelFactory):
    """"""
    class Meta:
        model = models.List


class ItemFactory(factory.DjangoModelFactory):
    """"""
    text = factory.Faker('sentence', nb_words=5)
    todo_list = factory.SubFactory(ListFactory)

    class Meta:
        model = models.Item
