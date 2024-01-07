import logging

from src.day7_camel_cards.camel_card_calculator import get_ranking_of_hand, calculate_ranking_value
from src.utilities.file_reader import read_lines_from_file

logger = logging.getLogger(__name__)


class CamelCardBid:
    def __init__(self, raw_hand_data, bid_amount):
        self.raw_hand_data = raw_hand_data
        self.bid_amount = bid_amount

        self.general_ranking, self.highest_card_ranking, self.second_highest_card_ranking \
            = get_ranking_of_hand(raw_hand_data)

        logger.warning(
            f"{raw_hand_data},{bid_amount},{self.general_ranking.name},{self.general_ranking},{self.highest_card_ranking},{self.second_highest_card_ranking}")

        self.value_of_hand = calculate_ranking_value(self.general_ranking,
                                                     self.highest_card_ranking,
                                                     self.second_highest_card_ranking)

        # logger.warning(f"Value of {raw_hand_data}: {self.value_of_hand}")


def order_bids_by_value_of_hand(camel_bid_list):
    return sorted(camel_bid_list, key=lambda bid: bid.value_of_hand)


def calculate_total_winnings(ordered_camel_bid_list: list[CamelCardBid]):
    total_winnings = 0
    current_bid_multiplier = 1
    for camel_card_bid in ordered_camel_bid_list:
        total_winnings += camel_card_bid.bid_amount * current_bid_multiplier
        logger.warning(f"Rank {current_bid_multiplier}, Hand: {camel_card_bid.raw_hand_data}, Bid: {camel_card_bid.bid_amount}, Total Bid: {total_winnings}, Details: ({camel_card_bid.general_ranking},{camel_card_bid.highest_card_ranking},{camel_card_bid.second_highest_card_ranking})")
        current_bid_multiplier += 1
    return total_winnings


def build_ordered_bids_by_value_of_hand(raw_camel_bid_list):
    bid_list = []
    for raw_bid in raw_camel_bid_list:
        raw_hand_data, raw_bid_amount = raw_bid.rstrip().split(" ")
        bid = CamelCardBid(raw_hand_data, int(raw_bid_amount))
        bid_list.append(bid)
    return order_bids_by_value_of_hand(bid_list)


def get_total_winnings_from_file(file_name):
    raw_camel_bid_list = read_lines_from_file(file_name)
    ordered_camel_bid_list = build_ordered_bids_by_value_of_hand(raw_camel_bid_list)
    return calculate_total_winnings(ordered_camel_bid_list)


if __name__ == '__main__':
    result = get_total_winnings_from_file(file_name="day7_data.txt")
    logger.warning(f"The total winnings are {result}")
    # 246838469 too low
    # 246728841 too low
    # 248184404 too high
