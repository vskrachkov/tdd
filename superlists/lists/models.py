from django.db import models


class Item(models.Model):
    """Items are the base of to-do lists. User can add items to to-do list,
    modify them if necessary or delete if they are completed.
    """
    text = models.TextField(verbose_name='Item text', max_length=300)

    def __repr__(self):
        return f'<Item: {self.text}>'

    def __str__(self):
        return f'Item: "{self.text}"'
