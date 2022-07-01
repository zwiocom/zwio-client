from unittest import TestCase
from zwio.companies import hello_world

class Test(TestCase):
    def test_hello_world(self):
        actual = hello_world("Daniel")
        expected = "Hello Daniel"
        self.assertEqual(actual, expected)
