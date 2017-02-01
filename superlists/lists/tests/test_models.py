from unittest import skip

from django.test import TestCase

from lists import factories
from lists.models import Item, List


class ListModelTest(TestCase):
    @skip
    def test_str_descriptor(self):
        pass

    @skip
    def test_repr_descriptor(self):
        pass


class ItemModelTest(TestCase):
    def test_str_descriptor(self):
        item = factories.ItemFactory()
        self.assertEqual(str(item), f'Item: {item.text}')

    def test_repr_descriptor(self):
        item = factories.ItemFactory()
        self.assertEqual(repr(item), f'Item: {item.text}')

    def test_save_item(self):
        item = factories.ItemFactory()
        self.assertEqual(item, Item.objects.first())
