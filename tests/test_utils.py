import unittest
import sys
sys.path.append('../src/')
from mailshot import utils

class TestUtils(unittest.TestCase):
    def test_to_list(self):
        self.assertEqual(utils.to_list("test"), ["test"])
        self.assertEqual(utils.to_list(["test", "test"]), ["test", "test"])


if __name__ == "__main__":
    unittest.main()