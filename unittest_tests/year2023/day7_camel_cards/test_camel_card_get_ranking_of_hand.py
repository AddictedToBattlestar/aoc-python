from unittest import TestCase
from src.year2023.day7_camel_cards.camel_card_calculator import get_ranking_of_hand, GeneralHandRanking


class TestGetRankingOfHand(TestCase):
    def test_five_of_a_kind(self):
        self.assertEqual((GeneralHandRanking.FIVE_OF_A_KIND, 14), get_ranking_of_hand("AAAAA"))
        self.assertEqual((GeneralHandRanking.FIVE_OF_A_KIND, 11), get_ranking_of_hand("JJJJJ"))

    def test_four_of_a_kind(self):
        self.assertEqual((GeneralHandRanking.FOUR_OF_A_KIND, 14), get_ranking_of_hand("AAAAK"))

    def test_full_house(self):
        self.assertEqual((GeneralHandRanking.FULL_HOUSE, 1413), get_ranking_of_hand("AAAKK"))
        self.assertEqual((GeneralHandRanking.FULL_HOUSE, 1413), get_ranking_of_hand("KKAAA"))
        self.assertEqual((GeneralHandRanking.FULL_HOUSE, 302), get_ranking_of_hand("22233"))
        self.assertEqual((GeneralHandRanking.FULL_HOUSE, 302), get_ranking_of_hand("33222"))
        self.assertEqual((GeneralHandRanking.FULL_HOUSE, 302), get_ranking_of_hand("23232"))
        self.assertEqual((GeneralHandRanking.FULL_HOUSE, 302), get_ranking_of_hand("32223"))

    def test_three_of_a_kind(self):
        self.assertEqual((GeneralHandRanking.THREE_OF_A_KIND, 14), get_ranking_of_hand("AAAKQ"))

    def test_one_pair(self):
        self.assertEqual((GeneralHandRanking.ONE_PAIR, 14), get_ranking_of_hand("AAKQJ"))
        self.assertEqual((GeneralHandRanking.ONE_PAIR, 3), get_ranking_of_hand("98733"))

    def test_two_pair(self):
        self.assertEqual((GeneralHandRanking.TWO_PAIR, 1413), get_ranking_of_hand("AAKKQ"))

    def test_high_card(self):
        self.assertEqual((GeneralHandRanking.HIGH_CARD, 60), get_ranking_of_hand("AKQJT"))
        self.assertEqual((GeneralHandRanking.HIGH_CARD, 25), get_ranking_of_hand("2345J"))
        self.assertEqual((GeneralHandRanking.HIGH_CARD, 37), get_ranking_of_hand("J345A"))
        self.assertEqual((GeneralHandRanking.HIGH_CARD, 52), get_ranking_of_hand("AQT97"))
        self.assertEqual((GeneralHandRanking.HIGH_CARD, 29), get_ranking_of_hand("98732"))

    def test_high_card_reversed(self):
        self.assertEqual((GeneralHandRanking.HIGH_CARD, 60), get_ranking_of_hand("TJQKA"))

    def test_high_card_scrambled(self):
        self.assertEqual((GeneralHandRanking.HIGH_CARD, 60), get_ranking_of_hand("KTQJA"))
