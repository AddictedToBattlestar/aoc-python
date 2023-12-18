from unittest import TestCase

from day6_wait_for_it.toy_boat_race_calculator import get_values, get_min_button_time, get_max_button_time, \
    get_number_of_ways_to_win, get_total_number_of_ways_to_win, get_total_number_of_ways_to_win_from_file


class Test(TestCase):
    def test_get_values(self):
        self.assertEqual([7, 15, 30], get_values("Time:      7  15   30"))
        self.assertEqual([9, 40, 200], get_values("Distance:  9  40  200"))

    def test_get_min_button_time(self):
        self.assertEqual(2, get_min_button_time(total_time_allowed=7, minimum_distance=9))
        self.assertEqual(4, get_min_button_time(total_time_allowed=15, minimum_distance=40))
        self.assertEqual(11, get_min_button_time(total_time_allowed=30, minimum_distance=200))

    def test_get_max_button_time(self):
        self.assertEqual(5, get_max_button_time(total_time_allowed=7, minimum_distance=9))
        self.assertEqual(11, get_max_button_time(total_time_allowed=15, minimum_distance=40))
        self.assertEqual(19, get_max_button_time(total_time_allowed=30, minimum_distance=200))

    def test_get_number_of_ways_to_win(self):
        self.assertEqual(4, get_number_of_ways_to_win(total_time_allowed=7, minimum_distance=9))
        self.assertEqual(8, get_number_of_ways_to_win(total_time_allowed=15, minimum_distance=40))
        self.assertEqual(9, get_number_of_ways_to_win(total_time_allowed=30, minimum_distance=200))

    def test_get_total_number_of_ways_to_win(self):
        self.assertEqual(288, get_total_number_of_ways_to_win(total_times_allowed=[7, 15, 30],
                                                              minimum_distances=[9, 40, 200]))

    def test_get_total_number_of_ways_to_win_from_file(self):
        self.assertEqual(288, get_total_number_of_ways_to_win_from_file("../day6_wait_for_it/day6_sample_data.txt"))
