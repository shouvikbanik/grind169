from unittest import TestCase

from valid_palindrome import valid_palindrome


class Test(TestCase):
    def test_valid_palindrome(self):
        self.assertTrue(valid_palindrome("hannah"))

    def test_valid_palindrome_negative(self):
        self.assertFalse(valid_palindrome("hnah"))
