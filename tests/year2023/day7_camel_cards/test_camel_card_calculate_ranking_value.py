from unittest import TestCase
from parameterized import parameterized

from src.year2023.day7_camel_cards.camel_card_calculator import GeneralHandRanking, calculate_ranking_value


class TestGetRanking(TestCase):
    @parameterized.expand([
        [70014, GeneralHandRanking.FIVE_OF_A_KIND, 14],
        [70013, GeneralHandRanking.FIVE_OF_A_KIND, 13],
        [70012, GeneralHandRanking.FIVE_OF_A_KIND, 12],
        [70011, GeneralHandRanking.FIVE_OF_A_KIND, 11],
        [70010, GeneralHandRanking.FIVE_OF_A_KIND, 10],
        [70009, GeneralHandRanking.FIVE_OF_A_KIND, 9],
        [70008, GeneralHandRanking.FIVE_OF_A_KIND, 8],
        [70007, GeneralHandRanking.FIVE_OF_A_KIND, 7],
        [70006, GeneralHandRanking.FIVE_OF_A_KIND, 6],
        [70005, GeneralHandRanking.FIVE_OF_A_KIND, 5],
        [70004, GeneralHandRanking.FIVE_OF_A_KIND, 4],
        [70003, GeneralHandRanking.FIVE_OF_A_KIND, 3],
        [70002, GeneralHandRanking.FIVE_OF_A_KIND, 2],

        [60014, GeneralHandRanking.FOUR_OF_A_KIND, 14],
        [60013, GeneralHandRanking.FOUR_OF_A_KIND, 13],
        [60012, GeneralHandRanking.FOUR_OF_A_KIND, 12],
        [60011, GeneralHandRanking.FOUR_OF_A_KIND, 11],
        [60010, GeneralHandRanking.FOUR_OF_A_KIND, 10],
        [60009, GeneralHandRanking.FOUR_OF_A_KIND, 9],
        [60008, GeneralHandRanking.FOUR_OF_A_KIND, 8],
        [60007, GeneralHandRanking.FOUR_OF_A_KIND, 7],
        [60006, GeneralHandRanking.FOUR_OF_A_KIND, 6],
        [60005, GeneralHandRanking.FOUR_OF_A_KIND, 5],
        [60004, GeneralHandRanking.FOUR_OF_A_KIND, 4],
        [60003, GeneralHandRanking.FOUR_OF_A_KIND, 3],
        [60002, GeneralHandRanking.FOUR_OF_A_KIND, 2],

        [40014, GeneralHandRanking.THREE_OF_A_KIND, 14],
        [40013, GeneralHandRanking.THREE_OF_A_KIND, 13],
        [40012, GeneralHandRanking.THREE_OF_A_KIND, 12],
        [40011, GeneralHandRanking.THREE_OF_A_KIND, 11],
        [40010, GeneralHandRanking.THREE_OF_A_KIND, 10],
        [40009, GeneralHandRanking.THREE_OF_A_KIND, 9],
        [40008, GeneralHandRanking.THREE_OF_A_KIND, 8],
        [40007, GeneralHandRanking.THREE_OF_A_KIND, 7],
        [40006, GeneralHandRanking.THREE_OF_A_KIND, 6],
        [40005, GeneralHandRanking.THREE_OF_A_KIND, 5],
        [40004, GeneralHandRanking.THREE_OF_A_KIND, 4],
        [40003, GeneralHandRanking.THREE_OF_A_KIND, 3],
        [40002, GeneralHandRanking.THREE_OF_A_KIND, 2],

        [30014, GeneralHandRanking.TWO_PAIR, 14],
        [30013, GeneralHandRanking.TWO_PAIR, 13],
        [30012, GeneralHandRanking.TWO_PAIR, 12],
        [30011, GeneralHandRanking.TWO_PAIR, 11],
        [30010, GeneralHandRanking.TWO_PAIR, 10],
        [30009, GeneralHandRanking.TWO_PAIR, 9],
        [30008, GeneralHandRanking.TWO_PAIR, 8],
        [30007, GeneralHandRanking.TWO_PAIR, 7],
        [30006, GeneralHandRanking.TWO_PAIR, 6],
        [30005, GeneralHandRanking.TWO_PAIR, 5],
        [30004, GeneralHandRanking.TWO_PAIR, 4],
        [30003, GeneralHandRanking.TWO_PAIR, 3],
        [30002, GeneralHandRanking.TWO_PAIR, 2],

        [20014, GeneralHandRanking.ONE_PAIR, 14],
        [20013, GeneralHandRanking.ONE_PAIR, 13],
        [20012, GeneralHandRanking.ONE_PAIR, 12],
        [20011, GeneralHandRanking.ONE_PAIR, 11],
        [20010, GeneralHandRanking.ONE_PAIR, 10],
        [20009, GeneralHandRanking.ONE_PAIR, 9],
        [20008, GeneralHandRanking.ONE_PAIR, 8],
        [20007, GeneralHandRanking.ONE_PAIR, 7],
        [20006, GeneralHandRanking.ONE_PAIR, 6],
        [20005, GeneralHandRanking.ONE_PAIR, 5],
        [20004, GeneralHandRanking.ONE_PAIR, 4],
        [20003, GeneralHandRanking.ONE_PAIR, 3],
        [20002, GeneralHandRanking.ONE_PAIR, 2],

        [10014, GeneralHandRanking.HIGH_CARD, 14],
        [10013, GeneralHandRanking.HIGH_CARD, 13],
        [10012, GeneralHandRanking.HIGH_CARD, 12],
        [10011, GeneralHandRanking.HIGH_CARD, 11],
        [10010, GeneralHandRanking.HIGH_CARD, 10],
        [10009, GeneralHandRanking.HIGH_CARD, 9],
        [10008, GeneralHandRanking.HIGH_CARD, 8],
        [10007, GeneralHandRanking.HIGH_CARD, 7],
        [10006, GeneralHandRanking.HIGH_CARD, 6],
        [10005, GeneralHandRanking.HIGH_CARD, 5],
        [10004, GeneralHandRanking.HIGH_CARD, 4],
        [10003, GeneralHandRanking.HIGH_CARD, 3],
        [10002, GeneralHandRanking.HIGH_CARD, 2]
    ])
    def test_ranking_calculator(self,
                                expected_ranking: int,
                                general_hand_ranking: GeneralHandRanking,
                                total_card_value:  int):
        self.assertEqual(expected_ranking,
                         calculate_ranking_value(general_hand_ranking,
                                                 total_card_value))

    @parameterized.expand([
        [50027, GeneralHandRanking.FULL_HOUSE, 27],
        [50025, GeneralHandRanking.FULL_HOUSE, 25],
        [50005, GeneralHandRanking.FULL_HOUSE, 5]
    ])
    def test_ranking_calculator_full_house(self,
                                           expected_ranking: int,
                                           general_hand_ranking: GeneralHandRanking,
                                           total_card_value: int):
        self.assertEqual(expected_ranking,
                         calculate_ranking_value(general_hand_ranking,
                                                 total_card_value))

    @parameterized.expand([
        [30027, GeneralHandRanking.TWO_PAIR, 27],
        [30025, GeneralHandRanking.TWO_PAIR, 25],
        [30005, GeneralHandRanking.TWO_PAIR, 5]
    ])
    def test_ranking_calculator_two_pair(self,
                                         expected_ranking: int,
                                         general_hand_ranking: GeneralHandRanking,
                                         total_card_value: int):
        self.assertEqual(expected_ranking,
                         calculate_ranking_value(general_hand_ranking,
                                                 total_card_value))
