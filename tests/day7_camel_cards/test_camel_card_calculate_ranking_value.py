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
        [714, GeneralHandRanking.FIVE_OF_A_KIND, 14],
        [713, GeneralHandRanking.FIVE_OF_A_KIND, 13],
        [712, GeneralHandRanking.FIVE_OF_A_KIND, 12],
        [711, GeneralHandRanking.FIVE_OF_A_KIND, 11],
        [710, GeneralHandRanking.FIVE_OF_A_KIND, 10],
        [709, GeneralHandRanking.FIVE_OF_A_KIND, 9],
        [708, GeneralHandRanking.FIVE_OF_A_KIND, 8],
        [707, GeneralHandRanking.FIVE_OF_A_KIND, 7],
        [706, GeneralHandRanking.FIVE_OF_A_KIND, 6],
        [705, GeneralHandRanking.FIVE_OF_A_KIND, 5],
        [704, GeneralHandRanking.FIVE_OF_A_KIND, 4],
        [703, GeneralHandRanking.FIVE_OF_A_KIND, 3],
        [702, GeneralHandRanking.FIVE_OF_A_KIND, 2],

        [614, GeneralHandRanking.FOUR_OF_A_KIND, 14],
        [613, GeneralHandRanking.FOUR_OF_A_KIND, 13],
        [612, GeneralHandRanking.FOUR_OF_A_KIND, 12],
        [611, GeneralHandRanking.FOUR_OF_A_KIND, 11],
        [610, GeneralHandRanking.FOUR_OF_A_KIND, 10],
        [609, GeneralHandRanking.FOUR_OF_A_KIND, 9],
        [608, GeneralHandRanking.FOUR_OF_A_KIND, 8],
        [607, GeneralHandRanking.FOUR_OF_A_KIND, 7],
        [606, GeneralHandRanking.FOUR_OF_A_KIND, 6],
        [605, GeneralHandRanking.FOUR_OF_A_KIND, 5],
        [604, GeneralHandRanking.FOUR_OF_A_KIND, 4],
        [603, GeneralHandRanking.FOUR_OF_A_KIND, 3],
        [602, GeneralHandRanking.FOUR_OF_A_KIND, 2],

        [414, GeneralHandRanking.THREE_OF_A_KIND, 14],
        [413, GeneralHandRanking.THREE_OF_A_KIND, 13],
        [412, GeneralHandRanking.THREE_OF_A_KIND, 12],
        [411, GeneralHandRanking.THREE_OF_A_KIND, 11],
        [410, GeneralHandRanking.THREE_OF_A_KIND, 10],
        [409, GeneralHandRanking.THREE_OF_A_KIND, 9],
        [408, GeneralHandRanking.THREE_OF_A_KIND, 8],
        [407, GeneralHandRanking.THREE_OF_A_KIND, 7],
        [406, GeneralHandRanking.THREE_OF_A_KIND, 6],
        [405, GeneralHandRanking.THREE_OF_A_KIND, 5],
        [404, GeneralHandRanking.THREE_OF_A_KIND, 4],
        [403, GeneralHandRanking.THREE_OF_A_KIND, 3],
        [402, GeneralHandRanking.THREE_OF_A_KIND, 2],

        [214, GeneralHandRanking.ONE_PAIR, 14],
        [213, GeneralHandRanking.ONE_PAIR, 13],
        [212, GeneralHandRanking.ONE_PAIR, 12],
        [211, GeneralHandRanking.ONE_PAIR, 11],
        [210, GeneralHandRanking.ONE_PAIR, 10],
        [209, GeneralHandRanking.ONE_PAIR, 9],
        [208, GeneralHandRanking.ONE_PAIR, 8],
        [207, GeneralHandRanking.ONE_PAIR, 7],
        [206, GeneralHandRanking.ONE_PAIR, 6],
        [205, GeneralHandRanking.ONE_PAIR, 5],
        [204, GeneralHandRanking.ONE_PAIR, 4],
        [203, GeneralHandRanking.ONE_PAIR, 3],
        [202, GeneralHandRanking.ONE_PAIR, 2],

        [114, GeneralHandRanking.HIGH_CARD, 14],
        [113, GeneralHandRanking.HIGH_CARD, 13],
        [112, GeneralHandRanking.HIGH_CARD, 12],
        [111, GeneralHandRanking.HIGH_CARD, 11],
        [110, GeneralHandRanking.HIGH_CARD, 10],
        [109, GeneralHandRanking.HIGH_CARD, 9],
        [108, GeneralHandRanking.HIGH_CARD, 8],
        [107, GeneralHandRanking.HIGH_CARD, 7],
        [106, GeneralHandRanking.HIGH_CARD, 6],
        [105, GeneralHandRanking.HIGH_CARD, 5],
        [104, GeneralHandRanking.HIGH_CARD, 4],
        [103, GeneralHandRanking.HIGH_CARD, 3],
        [102, GeneralHandRanking.HIGH_CARD, 2]
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
        [527, GeneralHandRanking.FULL_HOUSE, 27],
        [525, GeneralHandRanking.FULL_HOUSE, 25],
        [505, GeneralHandRanking.FULL_HOUSE, 5]
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
        [327, GeneralHandRanking.TWO_PAIR, 27],
        [325, GeneralHandRanking.TWO_PAIR, 25],
        [305, GeneralHandRanking.TWO_PAIR, 5]
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
