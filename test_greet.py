import unittest

from greet import greet


class GreetTests(unittest.TestCase):
    def test_greets_named_person(self):
        self.assertEqual(greet("Ada"), "Hello, Ada!")

    def test_greets_stranger_when_name_empty(self):
        self.assertEqual(greet(""), "Hello, stranger!")

    def test_greets_stranger_when_name_none(self):
        self.assertEqual(greet(None), "Hello, stranger!")


if __name__ == "__main__":
    unittest.main()
