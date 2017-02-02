from unittest import skip

from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):
    @skip
    def test_can_not_save_empty_list(self):
        pass
