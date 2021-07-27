import unittest
import os
import sys
sys.path.append('../src/')
from mailshot.client import Client

class TestClient(unittest.TestCase):
    def test_init(self):
        with self.assertRaises(ValueError):
            Client(email="test@example.com")

        with self.assertRaises(ValueError):
            Client(password="test")

        client = Client(email="test@example.com", password="test")
        self.assertEqual(client._email, "test@example.com")
        self.assertEqual(client._password, "test")

        if not (os.getenv('EMAIL') and os.getenv('PASSWORD')):
            with self.assertRaises(KeyError):
                Client()

    def test_get(self):
        client = Client(email="test@example.com", password="test")
        self.assertDictEqual(client._get(), {"EMAIL": "test@example.com", "PASSWORD": "test"})

    def test_set(self):
        if not (os.getenv('EMAIL') and os.getenv('PASSWORD')):
            with self.assertRaises(KeyError):
                Client()


if __name__ == "__main__":
    unittest.main()