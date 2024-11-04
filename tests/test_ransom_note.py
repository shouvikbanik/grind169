from unittest import TestCase

from ransom_note import ransom_note


class Test(TestCase):
    def test_ransom_note(self):
        self.assertTrue(ransom_note("a", "aaa"))
