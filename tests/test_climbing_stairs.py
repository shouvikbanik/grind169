from unittest import TestCase

from climbing_stairs import climbing_stairs


class Test(TestCase):
    def test_climbing_stairs(self):
        self.assertEqual(climbing_stairs(3), 3)
