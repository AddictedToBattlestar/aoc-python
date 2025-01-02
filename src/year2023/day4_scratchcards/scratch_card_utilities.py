from src.utilities.split_strip import split_strip
from src.utilities.split_strip_to_int import split_strip_to_int


def get_matching_numbers(card_numbers, winning_numbers):
    matching_numbers = []
    for number in card_numbers:
        if number in winning_numbers:
            matching_numbers.append(number)
    return matching_numbers


def get_numbers(raw_number_data):
    raw_winning_numbers, raw_card_numbers = split_strip(raw_number_data, "|")
    winning_numbers = split_strip_to_int(raw_winning_numbers, " ")
    card_numbers = split_strip_to_int(raw_card_numbers, " ")
    return winning_numbers, card_numbers


def get_card_number(raw_card_number) -> int:
    split_data = split_strip(raw_card_number, " ")
    return int(split_data[-1])