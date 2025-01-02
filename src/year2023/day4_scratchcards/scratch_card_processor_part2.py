import logging

from src.year2023.day4_scratchcards.scratch_card_utilities import get_card_number, get_numbers, get_matching_numbers
from src.utilities.split_strip import split_strip

logger = logging.getLogger(__name__)


class CardInfo:
    def __init__(self, card_number, matching_number_count):
        self.card_number = card_number
        self.matching_number_count = matching_number_count
        self.count = 1

    def add_more_copies(self, additional_count):
        self.count += additional_count


def calculate_from_file(file_name):
    with open(file_name, "r") as text_file:
        lines = text_file.readlines()
        return calculate_total_cards(lines)


def calculate_total_cards(starting_raw_cards):
    card_stack = []
    for raw_card in starting_raw_cards:
        raw_card_number, raw_number_data = split_strip(raw_card, ":")
        card_number = get_card_number(raw_card_number)
        matching_number_count = __count_matching_numbers(raw_number_data)
        new_card = CardInfo(card_number, matching_number_count)
        card_stack.append(new_card)

    total_cards = 0
    current_index = 0
    for card_info in card_stack:
        logger.info(
            f'Evaluating card: {card_info.card_number}, matching numbers count: {card_info.matching_number_count}, current number of copies: {card_info.count}')
        if card_info.matching_number_count > 0:
            for offset in range(1, card_info.matching_number_count + 1):
                if len(card_stack) > current_index + offset:
                    card_being_awarded = card_stack[current_index + offset]
                    logger.info(f'Awarding {card_info.count} copies of card number {card_being_awarded.card_number}')
                    card_being_awarded.count += card_info.count
        total_cards += card_info.count
        current_index += 1
    logger.info(f'Total number of cards now in the stack: {total_cards}')
    return total_cards


def __count_matching_numbers(raw_number_data):
    winning_numbers, card_numbers = get_numbers(raw_number_data)
    matching_numbers = get_matching_numbers(card_numbers, winning_numbers)
    return len(matching_numbers)


if __name__ == '__main__':
    result = calculate_from_file("day4-data.txt")
    logger.warning(f'The solution for Day 4 part 2 is: {result}')
