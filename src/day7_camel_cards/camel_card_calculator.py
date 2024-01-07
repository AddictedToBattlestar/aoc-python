from enum import IntEnum
from typing import Optional


class GeneralHandRanking(IntEnum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7

# A, 14
# K, 13
# Q, 12
# J, 11
# T, 10
# 9, 9
# ...


class CamelCardCounter:
    def __init__(self, card: str):
        self.card = card
        self.count = 0

    def increment(self):
        self.count += 1


def calculate_ranking_value(general_ranking: GeneralHandRanking, total_card_value: int):
    return general_ranking * 10000 + total_card_value


def get_ranking_of_hand(raw_hand_data) -> (GeneralHandRanking, int):
    card_map = build_card_map(raw_hand_data)

    first_hand_ranking_found, first_card_match = get_next_hand_ranking(card_map)
    if first_hand_ranking_found in [GeneralHandRanking.FIVE_OF_A_KIND, GeneralHandRanking.FOUR_OF_A_KIND]:
        return first_hand_ranking_found, get_rank_of_card(first_card_match)

    if first_hand_ranking_found == GeneralHandRanking.HIGH_CARD:
        total_card_value = 0
        for card in raw_hand_data:
            total_card_value += get_rank_of_card(card)
        return GeneralHandRanking.HIGH_CARD, total_card_value

    del card_map[first_card_match]

    second_hand_ranking_found, second_card_match = get_next_hand_ranking(card_map)
    if ((first_hand_ranking_found == GeneralHandRanking.THREE_OF_A_KIND
            and second_hand_ranking_found == GeneralHandRanking.ONE_PAIR)
        or first_hand_ranking_found == GeneralHandRanking.ONE_PAIR
            and second_hand_ranking_found == GeneralHandRanking.THREE_OF_A_KIND):
        return GeneralHandRanking.FULL_HOUSE, get_rank_of_card(first_card_match)*100 + get_rank_of_card(second_card_match)
    elif (first_hand_ranking_found == GeneralHandRanking.ONE_PAIR
          and second_hand_ranking_found == GeneralHandRanking.ONE_PAIR):
        return GeneralHandRanking.TWO_PAIR, get_rank_of_card(first_card_match)*100 + get_rank_of_card(second_card_match)
    else:
        return first_hand_ranking_found, get_rank_of_card(first_card_match)


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
    return GeneralHandRanking.HIGH_CARD, None


def is_high_card_hand(card_map) -> bool:
    for card in card_map:
        if card_map[card].count != 1:
            return False
    return True


def get_rank_of_card(card: Optional[str]):
    if card is None:
        return 0
    else:
        return "23456789TJQKA".index(card) + 2


def get_ranks_sorted(hand):
    return sorted(map(lambda card: get_rank_of_card(card), hand))
