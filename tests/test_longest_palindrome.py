from unittest import TestCase

from longest_palindrome import longest_palindrome


class Test(TestCase):
    def test_longest_palindrome(self):
        self.assertEqual(longest_palindrome("abccccdd"), 7)
