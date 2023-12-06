from unittest import TestCase
from utilities.split_strip_to_int import split_strip_to_int


class Test(TestCase):
    def test_split_strip_to_int(self):
        self.assertEqual([1, 2], split_strip_to_int("1,2", ","))
        self.assertEqual([1, 2], split_strip_to_int(" 1,2", ","))
        self.assertEqual([1, 2], split_strip_to_int("1 ,2", ","))
        self.assertEqual([1, 2], split_strip_to_int("1, 2", ","))
        self.assertEqual([1, 2], split_strip_to_int("1,2 ", ","))

    def test_split_strip_to_int_spaces(self):
        self.assertEqual([1, 2], split_strip_to_int("1 2", " "))
        self.assertEqual([1, 2], split_strip_to_int(" 1 2", " "))
        self.assertEqual([1, 2], split_strip_to_int("1  2", " "))
        self.assertEqual([1, 2], split_strip_to_int("1 2 ", " "))
