from unittest import TestCase

from parameterized import parameterized

from src.year2023.day7_camel_cards.camel_card_calculator import GeneralHandRanking
from src.year2023.day7_camel_cards.camel_card_processor import CamelCardBid, order_bids_by_value_of_hand, \
    build_ordered_bids_by_value_of_hand, get_total_winnings_from_file, calculate_total_winnings
from src.settings import PROJECT_ROOT


class TestCamelCardBid(TestCase):

    @parameterized.expand([
        ["AAAAA", 100, GeneralHandRanking.FIVE_OF_A_KIND, 14, 70014],
        ["AAAAK", 99, GeneralHandRanking.FOUR_OF_A_KIND, 14, 60014],
        ["99932", 98, GeneralHandRanking.THREE_OF_A_KIND, 9, 40009],
        ["98733", 97, GeneralHandRanking.ONE_PAIR, 3, 20003],
        ["JT987", 96, GeneralHandRanking.HIGH_CARD, 45, 10045],
        ["KKKQQ", 96, GeneralHandRanking.FULL_HOUSE, 1312, 51312],

    ])
    def test_creation(self,
                      raw_hand_data: str,
                      bid_amount: int,
                      hand_ranking: GeneralHandRanking,
                      total_card_value: int,
                      expected_value_of_hand: int):

        camel_bid = CamelCardBid(raw_hand_data, bid_amount)

        self.assertEqual(camel_bid.raw_hand_data, raw_hand_data)
        self.assertEqual(camel_bid.bid_amount, bid_amount)
        self.assertEqual(camel_bid.general_ranking, hand_ranking)
        self.assertEqual(camel_bid.total_card_value, total_card_value)
        self.assertEqual(camel_bid.value_of_hand, expected_value_of_hand)

    def test_processing_order(self):
        camel_bid1 = CamelCardBid("32T3K", 765)
        camel_bid2 = CamelCardBid("T55J5", 684)
        camel_bid3 = CamelCardBid("KK677", 28)
        camel_bid4 = CamelCardBid("KTJJT", 220)
        camel_bid5 = CamelCardBid("QQQJA", 483)
        camel_bid_list = [camel_bid1, camel_bid2, camel_bid3, camel_bid4, camel_bid5]

        ordered_camel_bid_list = order_bids_by_value_of_hand(camel_bid_list)

        self.assertEqual(ordered_camel_bid_list[0].raw_hand_data, camel_bid1.raw_hand_data)
        self.assertEqual(ordered_camel_bid_list[1].raw_hand_data, camel_bid4.raw_hand_data)
        self.assertEqual(ordered_camel_bid_list[2].raw_hand_data, camel_bid3.raw_hand_data)
        self.assertEqual(ordered_camel_bid_list[3].raw_hand_data, camel_bid2.raw_hand_data)
        self.assertEqual(ordered_camel_bid_list[4].raw_hand_data, camel_bid5.raw_hand_data)

    def test_camel_card_raw_data_processing(self):
        ordered_camel_bid_list = build_ordered_bids_by_value_of_hand([
            "32T3K 765",
            "T55J5 684",
            "KK677 28",
            "KTJJT 220",
            "QQQJA 483"
        ]);

        self.assertEqual(ordered_camel_bid_list[0].raw_hand_data, "32T3K")
        self.assertEqual(ordered_camel_bid_list[1].raw_hand_data, "KTJJT")
        self.assertEqual(ordered_camel_bid_list[2].raw_hand_data, "KK677")
        self.assertEqual(ordered_camel_bid_list[3].raw_hand_data, "T55J5")
        self.assertEqual(ordered_camel_bid_list[4].raw_hand_data, "QQQJA")

    def test_calculate_total_winnings(self):
        ordered_camel_bid_list = build_ordered_bids_by_value_of_hand([
            "32T3K 765",
            "T55J5 684",
            "KK677 28",
            "KTJJT 220",
            "QQQJA 483"
        ]);
        self.assertEqual(6440, calculate_total_winnings(ordered_camel_bid_list))

    def test_processing_from_file(self):
        sample_data_test_file = PROJECT_ROOT + "/year2023/day7_camel_cards/day7_sample_data.txt"
        total_winnings = get_total_winnings_from_file(sample_data_test_file)

        self.assertEqual(6440, total_winnings)

    def test_processing_from_file_example2(self):
        sample_data_test_file = PROJECT_ROOT + "/year2023/day7_camel_cards/day7_sample_data2.txt"
        total_winnings = get_total_winnings_from_file(sample_data_test_file)

        self.assertEqual(1343, total_winnings)

    # def test_processing_from_file_example3(self):
    #     # ref: https://www.reddit.com/r/adventofcode/comments/18cr4xr/2023_day_7_better_example_input_not_a_spoiler/
    #     sample_data_test_file = PROJECT_ROOT + "/year2023/day7_camel_cards/day7_sample_data3.txt"
    #     total_winnings = get_total_winnings_from_file(sample_data_test_file)
    #
    #     self.assertEqual(6592, total_winnings)