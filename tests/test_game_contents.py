from unittest import TestCase
from day2_cube_conundrum.game_contents import GameContents


class TestGameContents(TestCase):
    def test_game_contents(self):
        test1 = GameContents("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
        self.assertEqual(1, test1.id)
        self.assertEqual(4, test1.highest_red_count)
        self.assertEqual(2, test1.highest_green_count)
        self.assertEqual(6, test1.highest_blue_count)

        test2 = GameContents("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue")
        self.assertEqual(2, test2.id)
        self.assertEqual(1, test2.highest_red_count)
        self.assertEqual(3, test2.highest_green_count)
        self.assertEqual(4, test2.highest_blue_count)

        test3 = GameContents("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red")
        self.assertEqual(3, test3.id)
        self.assertEqual(20, test3.highest_red_count)
        self.assertEqual(13, test3.highest_green_count)
        self.assertEqual(6, test3.highest_blue_count)

        test4 = GameContents("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red")
        self.assertEqual(4, test4.id)
        self.assertEqual(14, test4.highest_red_count)
        self.assertEqual(3, test4.highest_green_count)
        self.assertEqual(15, test4.highest_blue_count)

        test5 = GameContents("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green")
        self.assertEqual(5, test5.id)
        self.assertEqual(6, test5.highest_red_count)
        self.assertEqual(3, test5.highest_green_count)
        self.assertEqual(2, test5.highest_blue_count)
