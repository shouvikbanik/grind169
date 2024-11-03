from unittest import TestCase

from binary_search import search


class Test(TestCase):
    def test_search(self):
        self.assertEqual(search([1, 2, 4, 5, 8, 3], 4), 2)
