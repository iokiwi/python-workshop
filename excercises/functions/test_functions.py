import unittest
from unittest import TestCase
from unittest.mock import patch
from io import StringIO
from functions import greet, greet_v2, greet_v3, add_to_cart


class TestFunctions(TestCase):
    @patch("sys.stdout", new_callable=StringIO)
    def test_greet(self, mock_stdout):
        greet("Alice")
        self.assertEqual("Hello, Alice!\n", mock_stdout.getvalue())

    @patch("sys.stdout", new_callable=StringIO)
    def test_greet_v2(self, mock_stdout):
        greet_v2("Alice")
        greet_v2("Bob", "Hallo")
        self.assertEqual("Hello, Alice!\nHallo, Bob!\n", mock_stdout.getvalue())

    @patch("sys.stdout", new_callable=StringIO)
    def test_greet_v3(self, mock_stdout):
        greet_v3("Alice", "Bob", greeting="Hallo")
        self.assertEqual(
            "Hallo, Alice!\nHallo, Bob!\n",
            mock_stdout.getvalue(),
        )

    def test_add_item_to_cart(self):
        _ = add_to_cart("Apples")
        cart2 = add_to_cart("Bananas")
        self.assertEqual(
            ["Bananas"], cart2
        )


if __name__ == "__main__":
    unittest.main()
