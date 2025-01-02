from unittest import TestCase
from src.year2023.day3_gear_ratios.grid_file_processor import process_file_for_sum_of_part_numbers
from src.settings import PROJECT_ROOT


class Test(TestCase):
    def test_process_file_for_sum_of_part_numbers(self):
        sample_data_test_file = PROJECT_ROOT + "/year2023/day3_gear_ratios/day3-part1-sample-data.txt"
        self.assertEqual(4361, process_file_for_sum_of_part_numbers(file_name=sample_data_test_file))

