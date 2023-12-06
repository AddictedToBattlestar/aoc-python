from unittest import TestCase
from day3_gear_ratios.grid_file_processor import process_file_for_sum_of_part_numbers


class Test(TestCase):
    def test_process_file_for_sum_of_part_numbers(self):
        self.assertEqual(4361, process_file_for_sum_of_part_numbers(file_name="../day3_gear_ratios/day3-part1-sample-data.txt"))

