from django.db import models


class List(models.Model):
    """List is a container of to-do items."""

    def __repr__(self):
        return f'List: consist of {self.items.all().count()} items'

    def __str__(self):
        return self.__repr__()


class Item(models.Model):
    """Items are the base of to-do lists. User creates items with tasks which
    it want to do later. User can add items to to-do list, modify them if
    necessary or delete if they are completed.
    """
    text = models.TextField(verbose_name='Item text', max_length=300)
    todo_list = models.ForeignKey(
        List, on_delete=models.CASCADE,
        related_name='items', related_query_name='item')

    def __repr__(self):
        return f'Item: {self.text}'

    def __str__(self):
        return self.__repr__()
