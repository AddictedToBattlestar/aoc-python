from enum import IntEnum
from typing import Optional


class GeneralHandRanking(IntEnum):
    UNKNOWN = 0
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7


class CamelCardCounter:
    def __init__(self, card: str):
        self.card = card
        self.count = 0

    def increment(self):
        self.count += 1


def calculate_ranking_value(general_ranking: GeneralHandRanking,
                            highest_card_ranking: Optional[str],
                            second_highest_card_ranking: Optional[str]) -> int:
    rank = general_ranking * 10000 + get_rank_of_card(highest_card_ranking) * 100
    if second_highest_card_ranking is not None:
        rank += get_rank_of_card(second_highest_card_ranking)
    return rank


def get_highest_card_in_hand(raw_hand_data):
    highest_card_ranking = get_rank_of_card(raw_hand_data[0])
    for card in raw_hand_data[1:]:
        rank = get_rank_of_card(card)
        if rank > highest_card_ranking:
            highest_card_ranking = rank
    return "23456789TJQKA"[highest_card_ranking]


def get_ranking_of_hand(raw_hand_data) -> (GeneralHandRanking, Optional[str], Optional[str]):
    card_map = build_card_map(raw_hand_data)

    first_hand_ranking_found, first_card_match = get_next_hand_ranking(card_map)
    if first_hand_ranking_found in [GeneralHandRanking.FIVE_OF_A_KIND, GeneralHandRanking.FOUR_OF_A_KIND]:
        return first_hand_ranking_found, first_card_match, None

    if first_hand_ranking_found == GeneralHandRanking.UNKNOWN:
        if is_high_card_hand(raw_hand_data):
            highest_rank_in_hand = get_ranks_sorted(raw_hand_data)[-1]
            highest_card_in_hand = "23456789TJQKA"[highest_rank_in_hand]
            return GeneralHandRanking.HIGH_CARD, highest_card_in_hand, None
        highest_card_in_hand = get_highest_card_in_hand(raw_hand_data)
        return GeneralHandRanking.UNKNOWN, highest_card_in_hand, None

    del card_map[first_card_match]

    second_hand_ranking_found, second_card_match = get_next_hand_ranking(card_map)
    if (first_hand_ranking_found == GeneralHandRanking.THREE_OF_A_KIND
            and second_hand_ranking_found == GeneralHandRanking.ONE_PAIR):
        return GeneralHandRanking.FULL_HOUSE, first_card_match, second_card_match
    elif (first_hand_ranking_found == GeneralHandRanking.ONE_PAIR
          and second_hand_ranking_found == GeneralHandRanking.ONE_PAIR):
        return GeneralHandRanking.TWO_PAIR, first_card_match, second_card_match
    else:
        return first_hand_ranking_found, first_card_match, None


def build_card_map(raw_hand_data):
    card_map = {}
    for card in raw_hand_data:
        if card not in card_map:
            card_map[card] = CamelCardCounter(card)
        card_map[card].increment()
    return card_map


def get_next_hand_ranking(card_map):
    for card in "AKQJT98764532":
        if card in card_map:
            if card_map[card].count == 5:
                return GeneralHandRanking.FIVE_OF_A_KIND, card
            if card_map[card].count == 4:
                return GeneralHandRanking.FOUR_OF_A_KIND, card
            if card_map[card].count == 3:
                return GeneralHandRanking.THREE_OF_A_KIND, card
            if card_map[card].count == 2:
                return GeneralHandRanking.ONE_PAIR, card
    return GeneralHandRanking.UNKNOWN, None


def is_high_card_hand(hand) -> bool:
    ranks_in_hand = get_ranks_sorted(hand)
    previous_rank = ranks_in_hand[0]
    for current_rank in ranks_in_hand[1:]:
        if previous_rank + 1 != current_rank:
            return False
        previous_rank = current_rank
    return True


def get_rank_of_card(card: Optional[str]):
    if card is None:
        return 0
    else:
        return "23456789TJQKA".index(card)


def get_ranks_sorted(hand):
    return sorted(map(lambda card: get_rank_of_card(card), hand))
