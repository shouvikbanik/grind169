from unittest import TestCase

from valid_anagram import is_anagram


class Test(TestCase):
    def test_is_anagram(self):
        self.assertTrue(is_anagram("abdc", "abcd"))
