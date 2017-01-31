from unittest import skip

from django.core.urlresolvers import resolve
from django.db import IntegrityError
from django.test import TestCase
from django.http import HttpRequest

from faker import Faker

from .views import home_page
from . import factories
from .models import Item

fake = Faker()


def post_request(post_dict=None):
    request = HttpRequest()
    request.method = 'POST'
    if post_dict:
        request.POST.update(post_dict)
    return request


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_no_items_on_home_page(self):
        response = home_page(HttpRequest())
        self.assertIn('No items.', response.content.decode())

    def test_home_page_can_save_POST(self):
        item_text = fake.sentence(nb_words=5)
        home_page(post_request({'item_text': item_text}))
        item = Item.objects.first()
        self.assertTrue(item, msg='Item did not saved.')
        self.assertEqual(Item.objects.first().text, item_text)
        self.assertEqual(Item.objects.all().count(), 1)

    def test_redirect_after_POST(self):
        response = home_page(
            post_request({'item_text': fake.sentence(nb_words=5)})
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/')


class ItemModelTest(TestCase):
    def test_str_descriptor(self):
        item = factories.ItemFactory()
        self.assertEqual(str(item), f'Item: "{item.text}"')

    def test_repr_descriptor(self):
        item = factories.ItemFactory()
        self.assertEqual(repr(item), f'<Item: {item.text}>')

    def test_save_item(self):
        item = factories.ItemFactory()
        self.assertEqual(item, Item.objects.first())
