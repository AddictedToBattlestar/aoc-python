from unittest import TestCase

from day2_cube_conundrum.bag_contents import BagContents
from day2_cube_conundrum.game_file_processor import process_file


class Test(TestCase):
    def test_process_file(self):
        bag_contents = BagContents(12, 13, 14)
        self.assertEqual(8, process_file(file_name="../day2_cube_conundrum/day1-part1-sample.data.txt", bag_contents=bag_contents))
