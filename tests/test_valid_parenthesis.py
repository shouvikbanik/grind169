from unittest import TestCase

from valid_parenthesis import valid_parenthesis


class Test(TestCase):
    def test_valid_parenthesis(self):
        self.assertTrue(valid_parenthesis("(([{}]))"))

    def test_valid_parenthesis_negative(self):
        self.assertFalse(valid_parenthesis("(([{}])"))
