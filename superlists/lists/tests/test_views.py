from django.core.urlresolvers import resolve
from django.test import TestCase
from django.urls import reverse

from faker import Faker

from lists.factories import ItemFactory, ListFactory
from lists.views import home_page, lists_view, new_item, add_item
from lists.models import Item, List

fake = Faker()

# todo: Rewrite all 'reverse' functions to format strings.


class HomePageViewTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)


class ListViewTest(TestCase):
    def test_display_all_items(self):
        a_list = ListFactory()
        items = ItemFactory.create_batch(size=2, todo_list=a_list)
        response = self.client.get(
            reverse(lists_view, kwargs={'list_id': a_list.id})
        )
        self.assertContains(response, items[0].text)
        self.assertContains(response, items[1].text)

    def test_uses_right_template(self):
        a_list = List.objects.create()
        response = self.client.get(
            reverse(lists_view, kwargs={'list_id': a_list.id})
        )
        self.assertTemplateUsed(response, 'lists/list.html')

    def test_display_correct_items(self):
        items = ItemFactory.create_batch(size=2)
        response = self.client.get(
            reverse(lists_view, kwargs={'list_id': items[0].id})
        )
        assert items[0].text != items[1].text
        self.assertContains(response, items[0].text)
        self.assertNotContains(response, items[1].text)


class NewItemViewTest(TestCase):
    def test_can_save_POST(self):
        item_text = fake.sentence(nb_words=5)
        self.client.post(reverse(new_item), {'item_text': item_text})
        item = Item.objects.first()
        self.assertTrue(item, msg='Item did not saved.')
        self.assertEqual(Item.objects.first().text, item_text)
        self.assertEqual(Item.objects.all().count(), 1)

    def test_redirect_after_POST(self):
        response = self.client.post(reverse(new_item),
                                    {'item_text': fake.sentence(nb_words=5)})
        self.assertEqual(response.status_code, 302)


class AddNewItemTest(TestCase):
    def test_add_new_item_to_existing_list(self):
        a_list = ListFactory()
        item_text = fake.sentence(nb_words=5)
        self.client.post(
            reverse(add_item,
                    kwargs={'list_id': a_list.id}),
            {'item_text': item_text}
        )
        self.assertEqual(
            item_text, Item.objects.get(todo_list_id=a_list.id).text
        )

    def test_redirect_to_correct_page(self):
        a_list = ListFactory()
        item_text = fake.sentence(nb_words=5)
        response = self.client.post(
            reverse(add_item,
                    kwargs={'list_id': a_list.id}),
            {'item_text': item_text}
        )
        self.assertRedirects(response, f'/lists/{a_list.id}/')
