from unittest import TestCase

from implement_queue_using_stacks import MyQueue


class TestMyQueue(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.obj = MyQueue()

    def test_push_pop(self):
        self.obj.push(10)
        self.assertEqual(self.obj.pop(), 10)

    def test_peek(self):
        self.obj.push(30)
        self.assertEqual(self.obj.peek(), 30)
        self.obj.pop()

    def test_empty(self):
        self.assertTrue(self.obj.empty())
