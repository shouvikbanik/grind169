from unittest import TestCase

from first_bad_version import first_bad_version, CheckVersion


class Test(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.obj = CheckVersion()

    def test_first_bad_version(self):
        self.assertEqual(first_bad_version(self.obj, 5), 4)

    def test_first_bad_version_call_count(self):
        self.assertEqual(self.obj.count, 2)
