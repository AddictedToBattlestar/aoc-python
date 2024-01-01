from unittest import TestCase
from src.day2_cube_conundrum.power_of_sets_game_tracker import PowerOfSetsGameTracker


class TestPowerOfSetsGameTracker(TestCase):
    def test_process_power_of_sets(self):
        subject = PowerOfSetsGameTracker()
        power, sum_of_power = subject.process_power_of_sets("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
        self.assertEqual(48, power)
        self.assertEqual(48, sum_of_power)
        power, sum_of_power = subject.process_power_of_sets(
            "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue")
        self.assertEqual(12, power)
        self.assertEqual(60, sum_of_power)
        power, sum_of_power = subject.process_power_of_sets(
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red")
        self.assertEqual(1560, power)
        self.assertEqual(1620, sum_of_power)
        power, sum_of_power = subject.process_power_of_sets(
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red")
        self.assertEqual(630, power)
        self.assertEqual(2250, sum_of_power)
        power, sum_of_power = subject.process_power_of_sets("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green")
        self.assertEqual(36, power)
        self.assertEqual(2286, sum_of_power)
