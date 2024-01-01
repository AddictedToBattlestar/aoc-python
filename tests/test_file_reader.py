from unittest import TestCase

from utilities.file_reader import read_lines_from_file


class Test(TestCase):
    def test_read_lines_from_file(self):
        self.assertEqual(["123", "456", "789"], read_lines_from_file("test_file_reader_test_data.txt"))
