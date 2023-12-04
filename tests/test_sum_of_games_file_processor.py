from unittest import TestCase

from day2_cube_conundrum.bag_contents import BagContents
from day2_cube_conundrum.sum_of_games_file_processor import process_file_for_sum_of_game


class Test(TestCase):
    def test_process_file(self):
        bag_contents = BagContents(12, 13, 14)
        self.assertEqual(8, process_file_for_sum_of_game(file_name="../day2_cube_conundrum/day1-part1-sample.data.txt", bag_contents=bag_contents))
