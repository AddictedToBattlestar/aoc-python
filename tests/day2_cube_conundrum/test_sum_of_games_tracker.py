from unittest import TestCase

from src.day2_cube_conundrum.bag_contents import BagContents
from src.day2_cube_conundrum.sum_of_game_tracker import SumOfGameTracker


class TestGameTracker(TestCase):
    def test_process_sum_of_games_possible(self):
        bag_contents = BagContents(12, 13, 14)
        game_tracker = SumOfGameTracker(bag_contents)
        result = game_tracker.process_sum_of_games_possible("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
        self.assertEqual(1, result)
        result = game_tracker.process_sum_of_games_possible(
            "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue")
        self.assertEqual(3, result)
        result = game_tracker.process_sum_of_games_possible(
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red")
        self.assertEqual(3, result)
        result = game_tracker.process_sum_of_games_possible(
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red")
        self.assertEqual(3, result)
        result = game_tracker.process_sum_of_games_possible("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green")
        self.assertEqual(8, result)