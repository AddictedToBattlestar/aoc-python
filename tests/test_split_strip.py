from unittest import TestCase
from utilities.split_strip import split_strip


class Test(TestCase):
    def test_split_strip(self):
        self.assertEqual(["foo", "bar"], split_strip("foo,bar", ","))
        self.assertEqual(["foo", "bar"], split_strip(" foo,bar", ","))
        self.assertEqual(["foo", "bar"], split_strip("foo ,bar", ","))
        self.assertEqual(["foo", "bar"], split_strip("foo, bar", ","))
        self.assertEqual(["foo", "bar"], split_strip("foo,bar ", ","))
