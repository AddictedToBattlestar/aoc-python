from day7_camel_cards.camel_card_calculator import get_ranking_of_hand, calculate_ranking_value


class CamelCardBid:
    def __init__(self, raw_hand_data, bid_amount):
        self.raw_hand_data = raw_hand_data
        self.bid_amount = bid_amount

        self.general_ranking, self.highest_card_ranking, self.second_highest_card_ranking \
            = get_ranking_of_hand(raw_hand_data)
        print(f"General ranking of {raw_hand_data}: {self.general_ranking}, {self.highest_card_ranking}, {self.second_highest_card_ranking}")

        self.value_of_hand = calculate_ranking_value(self.general_ranking,
                                                     self.highest_card_ranking,
                                                     self.second_highest_card_ranking)

        print(f"Value of {raw_hand_data}: {self.value_of_hand}")



def order_bids_by_value_of_hand(camel_bid_list):
    return sorted(camel_bid_list, key=lambda bid: bid.value_of_hand)


def calculate_total_winnings(ordered_camel_bid_list):
    total_winnings = 0
    current_bid_multiplier = 1
    for camel_card_bid in ordered_camel_bid_list:
        total_winnings += camel_card_bid.bid_amount * current_bid_multiplier
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
    with open(file_name, "r") as text_file:
        raw_camel_bid_list = text_file.readlines()
        ordered_camel_bid_list = build_ordered_bids_by_value_of_hand(raw_camel_bid_list)
        return calculate_total_winnings(ordered_camel_bid_list)


if __name__ == '__main__':
    result = get_total_winnings_from_file(file_name="day7_data.txt")
    print(f"The total winnings are {result}")
    # 246838469 too low

