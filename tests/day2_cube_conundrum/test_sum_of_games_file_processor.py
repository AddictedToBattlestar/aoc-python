from unittest import TestCase

from src.day2_cube_conundrum.bag_contents import BagContents
from src.day2_cube_conundrum.sum_of_games_file_processor import process_file_for_sum_of_game
from src.settings import PROJECT_ROOT


class Test(TestCase):
    def test_process_file(self):
        sample_data_test_file = PROJECT_ROOT + "/day2_cube_conundrum/day2-part1-sample-data.txt"
        bag_contents = BagContents(12, 13, 14)
        self.assertEqual(8, process_file_for_sum_of_game(file_name=sample_data_test_file, bag_contents=bag_contents))
