from unittest import TestCase

from src.utilities.file_reader import read_lines_from_file
from tests.test_settings import TEST_PROJECT_ROOT


class Test(TestCase):
    def test_read_lines_from_file(self):
        path_to_this_test_file = TEST_PROJECT_ROOT + "/utilities/test_file_reader_test_data.txt"
        self.assertEqual(["123", "456", "789"],
                         (read_lines_from_file(path_to_this_test_file)))
