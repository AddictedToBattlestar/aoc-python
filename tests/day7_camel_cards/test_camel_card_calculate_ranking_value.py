from unittest import TestCase
from parameterized import parameterized

from src.day7_camel_cards.camel_card_calculator import GeneralHandRanking, calculate_ranking_value

'''
Ranking notes:
GeneralHandRanking * 100 + highest_card_ranking + second_highest_card_ranking
AAAAA: (7 * 10000) + (12 * 100) = 71200
KKKKK:(7 * 10000) + (11 * 100) = 71100

AAAAK: (6 * 10000) + (12 * 100) = 61200
QQQQA: (6 * 10000) + (10 * 100) = 61100

AAAKK: (5 * 10000) + (12 * 100) + 11 = 51211
KKKQQ: (5 * 10000) + (11 * 100) + 10 = 51101
33322: (5 * 10000) + (1 * 100) + 0 =   50100 

AAKKQ: (3 * 10000) + (12 * 100) + 11 = 31211
KKQQJ: (3 * 10000) + (11 * 100) + 10 = 31110
'''


class TestGetRanking(TestCase):
    @parameterized.expand([
        [71200, GeneralHandRanking.FIVE_OF_A_KIND, "A"],
        [71100, GeneralHandRanking.FIVE_OF_A_KIND, "K"],
        [71000, GeneralHandRanking.FIVE_OF_A_KIND, "Q"],
        [70900, GeneralHandRanking.FIVE_OF_A_KIND, "J"],
        [70800, GeneralHandRanking.FIVE_OF_A_KIND, "T"],
        [70700, GeneralHandRanking.FIVE_OF_A_KIND, "9"],
        [70600, GeneralHandRanking.FIVE_OF_A_KIND, "8"],
        [70500, GeneralHandRanking.FIVE_OF_A_KIND, "7"],
        [70400, GeneralHandRanking.FIVE_OF_A_KIND, "6"],
        [70300, GeneralHandRanking.FIVE_OF_A_KIND, "5"],
        [70200, GeneralHandRanking.FIVE_OF_A_KIND, "4"],
        [70100, GeneralHandRanking.FIVE_OF_A_KIND, "3"],
        [70000, GeneralHandRanking.FIVE_OF_A_KIND, "2"],

        [61200, GeneralHandRanking.FOUR_OF_A_KIND, "A"],
        [61100, GeneralHandRanking.FOUR_OF_A_KIND, "K"],
        [61000, GeneralHandRanking.FOUR_OF_A_KIND, "Q"],
        [60900, GeneralHandRanking.FOUR_OF_A_KIND, "J"],
        [60800, GeneralHandRanking.FOUR_OF_A_KIND, "T"],
        [60700, GeneralHandRanking.FOUR_OF_A_KIND, "9"],
        [60600, GeneralHandRanking.FOUR_OF_A_KIND, "8"],
        [60500, GeneralHandRanking.FOUR_OF_A_KIND, "7"],
        [60400, GeneralHandRanking.FOUR_OF_A_KIND, "6"],
        [60300, GeneralHandRanking.FOUR_OF_A_KIND, "5"],
        [60200, GeneralHandRanking.FOUR_OF_A_KIND, "4"],
        [60100, GeneralHandRanking.FOUR_OF_A_KIND, "3"],
        [60000, GeneralHandRanking.FOUR_OF_A_KIND, "2"],

        [41200, GeneralHandRanking.THREE_OF_A_KIND, "A"],
        [41100, GeneralHandRanking.THREE_OF_A_KIND, "K"],
        [41000, GeneralHandRanking.THREE_OF_A_KIND, "Q"],
        [40900, GeneralHandRanking.THREE_OF_A_KIND, "J"],
        [40800, GeneralHandRanking.THREE_OF_A_KIND, "T"],
        [40700, GeneralHandRanking.THREE_OF_A_KIND, "9"],
        [40600, GeneralHandRanking.THREE_OF_A_KIND, "8"],
        [40500, GeneralHandRanking.THREE_OF_A_KIND, "7"],
        [40400, GeneralHandRanking.THREE_OF_A_KIND, "6"],
        [40300, GeneralHandRanking.THREE_OF_A_KIND, "5"],
        [40200, GeneralHandRanking.THREE_OF_A_KIND, "4"],
        [40100, GeneralHandRanking.THREE_OF_A_KIND, "3"],
        [40000, GeneralHandRanking.THREE_OF_A_KIND, "2"],

        [21200, GeneralHandRanking.ONE_PAIR, "A"],
        [21100, GeneralHandRanking.ONE_PAIR, "K"],
        [21000, GeneralHandRanking.ONE_PAIR, "Q"],
        [20900, GeneralHandRanking.ONE_PAIR, "J"],
        [20800, GeneralHandRanking.ONE_PAIR, "T"],
        [20700, GeneralHandRanking.ONE_PAIR, "9"],
        [20600, GeneralHandRanking.ONE_PAIR, "8"],
        [20500, GeneralHandRanking.ONE_PAIR, "7"],
        [20400, GeneralHandRanking.ONE_PAIR, "6"],
        [20300, GeneralHandRanking.ONE_PAIR, "5"],
        [20200, GeneralHandRanking.ONE_PAIR, "4"],
        [20100, GeneralHandRanking.ONE_PAIR, "3"],
        [20000, GeneralHandRanking.ONE_PAIR, "2"],

        [11200, GeneralHandRanking.HIGH_CARD, "A"],
        [11100, GeneralHandRanking.HIGH_CARD, "K"],
        [11000, GeneralHandRanking.HIGH_CARD, "Q"],
        [10900, GeneralHandRanking.HIGH_CARD, "J"],
        [10800, GeneralHandRanking.HIGH_CARD, "T"],
        [10700, GeneralHandRanking.HIGH_CARD, "9"],
        [10600, GeneralHandRanking.HIGH_CARD, "8"],
        [10500, GeneralHandRanking.HIGH_CARD, "7"],
        [10400, GeneralHandRanking.HIGH_CARD, "6"],
        [10300, GeneralHandRanking.HIGH_CARD, "5"],
        [10200, GeneralHandRanking.HIGH_CARD, "4"],
        [10100, GeneralHandRanking.HIGH_CARD, "3"],
        [10000, GeneralHandRanking.HIGH_CARD, "2"]
    ])
    def test_ranking_calculator(self,
                                expected_ranking: int,
                                general_hand_ranking: GeneralHandRanking,
                                highest_card_ranking: str):
        self.assertEqual(expected_ranking,
                         calculate_ranking_value(general_hand_ranking,
                                                 highest_card_ranking,
                                                 None))

    @parameterized.expand([
        [51211, GeneralHandRanking.FULL_HOUSE, "A", "K"],
        [51110, GeneralHandRanking.FULL_HOUSE, "K", "Q"],
        [50100, GeneralHandRanking.FULL_HOUSE, "3", "2"]
    ])
    def test_ranking_calculator_full_house(self,
                                           expected_ranking: int,
                                           general_hand_ranking: GeneralHandRanking,
                                           highest_card_ranking: str,
                                           second_highest_card_ranking: str):
        self.assertEqual(expected_ranking,
                         calculate_ranking_value(general_hand_ranking,
                                                 highest_card_ranking,
                                                 second_highest_card_ranking))

    @parameterized.expand([
        [31211, GeneralHandRanking.TWO_PAIR, "A", "K"],
        [31110, GeneralHandRanking.TWO_PAIR, "K", "Q"],
        [30100, GeneralHandRanking.TWO_PAIR, "3", "2"]
    ])
    def test_ranking_calculator_two_pair(self,
                                         expected_ranking: int,
                                         general_hand_ranking: GeneralHandRanking,
                                         highest_card_ranking: str,
                                         second_highest_card_ranking: str):
        self.assertEqual(expected_ranking,
                         calculate_ranking_value(general_hand_ranking,
                                                 highest_card_ranking,
                                                 second_highest_card_ranking))
