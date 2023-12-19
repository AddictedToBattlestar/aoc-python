from unittest import TestCase
from day7_camel_cards.camel_card_calculator import get_ranking_of_hand, GeneralHandRanking


class TestGetRankingOfHand(TestCase):
    def test_five_of_a_kind(self):
        self.assertEqual((GeneralHandRanking.FIVE_OF_A_KIND, "A", None), get_ranking_of_hand("AAAAA"))

    def test_four_of_a_kind(self):
        self.assertEqual((GeneralHandRanking.FOUR_OF_A_KIND, "A", None), get_ranking_of_hand("AAAAK"))

    def test_full_house(self):
        self.assertEqual((GeneralHandRanking.FULL_HOUSE, "A", "K"), get_ranking_of_hand("AAAKK"))
        self.assertEqual((GeneralHandRanking.FULL_HOUSE, "A", "K"), get_ranking_of_hand("KKAAA"))

    def test_three_of_a_kind(self):
        self.assertEqual((GeneralHandRanking.THREE_OF_A_KIND, "A", None), get_ranking_of_hand("AAAKQ"))

    def test_one_pair(self):
        self.assertEqual((GeneralHandRanking.ONE_PAIR, "A", None), get_ranking_of_hand("AAKQJ"))
        self.assertEqual((GeneralHandRanking.ONE_PAIR, "3", None), get_ranking_of_hand("98733"))

    def test_two_pair(self):
        self.assertEqual((GeneralHandRanking.TWO_PAIR, "A", "K"), get_ranking_of_hand("AAKKQ"))

    def test_high_card(self):
        self.assertEqual((GeneralHandRanking.HIGH_CARD, "A", None), get_ranking_of_hand("AKQJT"))

    def test_high_card_reversed(self):
        self.assertEqual((GeneralHandRanking.HIGH_CARD, "A", None), get_ranking_of_hand("TJQKA"))

    def test_high_card_scrambled(self):
        self.assertEqual((GeneralHandRanking.HIGH_CARD, "A", None), get_ranking_of_hand("KTQJA"))

    def test_unknown(self):
        self.assertEqual((GeneralHandRanking.UNKNOWN, None, None), get_ranking_of_hand("AQT97"))
