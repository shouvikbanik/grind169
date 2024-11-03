from unittest import TestCase

from flood_fill import flood_fill


class Test(TestCase):
    def test_flood_fill(self):
        self.assertEqual(flood_fill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2), [[2, 2, 2], [2, 2, 0], [2, 0, 1]])
