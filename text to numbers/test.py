import unittest
from io import StringIO
import sys

# Import the functions directly (or place them in a module and import from there)
from main import run  # Replace with the correct module name if needed

class TestTextToNumber(unittest.TestCase):

    def test_basic_numbers(self):
        self.assertEqual(run("one"), 1)
        self.assertEqual(run("ten"), 10)
        self.assertEqual(run("twenty"), 20)

    def test_composite_numbers(self):
        self.assertEqual(run("twenty one"), 21)
        self.assertEqual(run("ninety nine"), 99)
        self.assertEqual(run("forty three"), 43)

    def test_hundreds(self):
        self.assertEqual(run("one hundred"), 100)
        self.assertEqual(run("three hundred"), 300)
        self.assertEqual(run("one hundred twenty three"), 123)

    def test_thousands(self):
        self.assertEqual(run("one thousand"), 1000)
        self.assertEqual(run("two thousand fifty"), 2050)
        self.assertEqual(run("three thousand one hundred twelve"), 3112)

    def test_large_numbers(self):
        self.assertEqual(run("one million"), 1000000)
        self.assertEqual(run("one million one hundred thousand"), 1100000)

    def test_invalid_input(self):
        self.assertEqual(run("gibberish words"), 0)
        self.assertEqual(run("one apple two oranges"),0)

if __name__ == '__main__':
    unittest.main()
