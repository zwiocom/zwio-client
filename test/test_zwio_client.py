from unittest import TestCase
from src.zwio_client import hello_world

class Test(TestCase):
    def test_hello_world(self):
        actual = hello_world("Daniel")
        expected = "Hello Daniel"
        self.assertEqual(actual, expected)
