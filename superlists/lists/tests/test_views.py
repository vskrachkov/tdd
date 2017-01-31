from django.core.urlresolvers import resolve
from django.test import TestCase
from django.urls import reverse

from faker import Faker

from lists.factories import ItemFactory
from lists.views import home_page, lists_view, new_item
from lists.models import Item

fake = Faker()


class HomePageViewTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)


class ListViewTest(TestCase):
    def test_display_all_items(self):
        items = ItemFactory.create_batch(size=2)
        response = self.client.get('/lists/only-one')
        self.assertContains(response, items[0].text)
        self.assertContains(response, items[1].text)

    def test_uses_right_template(self):
        response = self.client.get(reverse(lists_view))
        self.assertTemplateUsed(response, 'lists/list.html')


class NewListTest(TestCase):
    def test_can_save_POST(self):
        item_text = fake.sentence(nb_words=5)
        self.client.post(reverse(new_item), {'item_text': item_text})
        item = Item.objects.first()
        self.assertTrue(item, msg='Item did not saved.')
        self.assertEqual(Item.objects.first().text, item_text)
        self.assertEqual(Item.objects.all().count(), 1)

    def test_redirect_after_POST(self):
        response = self.client.post(reverse(home_page),
                                    {'item_text': fake.sentence(nb_words=5)})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse(lists_view))
