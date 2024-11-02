from unittest import TestCase

from two_sum import two_sum


class Test(TestCase):
    def test_two_sum(self):
        i, j = two_sum([1, 2, 6, 7, 3], 10)
        self.assertTrue((i == 3 and j == 4) or (i == 4 and j == 3))
