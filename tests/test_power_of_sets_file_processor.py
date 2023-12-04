from unittest import TestCase
from day2_cube_conundrum.power_of_sets_file_processor import process_file_for_power_of_sets

class Test(TestCase):
    def test_process_file_for_power_of_sets(self):
        self.assertEqual(2286, process_file_for_power_of_sets(file_name="../day2_cube_conundrum/day1-part1-sample.data.txt"))

