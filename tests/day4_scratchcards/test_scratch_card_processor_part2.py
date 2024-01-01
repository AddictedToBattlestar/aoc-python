from unittest import TestCase
from src.day4_scratchcards.scratch_card_processor_part2 import calculate_total_cards, calculate_from_file
from src.settings import PROJECT_ROOT


class Test(TestCase):
    def test_calculate_total_cards(self):
        self.assertEqual(30, calculate_total_cards([
            "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
            "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
            "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
            "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
            "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
            "Card  6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"
        ]))

    def test_calculate_from_file(self):
        sample_data_test_file = PROJECT_ROOT + "/day4_scratchcards/day4-sample-data.txt"
        self.assertEqual(30, calculate_from_file(sample_data_test_file))
