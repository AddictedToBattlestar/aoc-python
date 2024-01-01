import pathlib
from unittest import TestCase
from src.day2_cube_conundrum.power_of_sets_file_processor import process_file_for_power_of_sets
from src.settings import PROJECT_ROOT


class Test(TestCase):
    def test_process_file_for_power_of_sets(self):
        sample_data_test_file = PROJECT_ROOT + "/day2_cube_conundrum/day2-part1-sample-data.txt"
        self.assertEqual(2286, process_file_for_power_of_sets(
            file_name=sample_data_test_file))
