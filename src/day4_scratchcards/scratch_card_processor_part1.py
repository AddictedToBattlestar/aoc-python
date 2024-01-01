import logging

from src.day4_scratchcards.scratch_card_utilities import get_numbers, get_matching_numbers, get_card_number
from src.utilities.split_strip import split_strip

logger = logging.getLogger(__name__)


def calculate_from_file(file_name):
    with open(file_name, "r") as text_file:
        lines = text_file.readlines()
        return calculate_total_points(lines)


def calculate_total_points(raw_cards):
    points = 0
    for raw_card in raw_cards:
        points += get_winning_numbers(raw_card)
    return points


def get_winning_numbers(raw_card_data):
    raw_card_number, raw_number_data = split_strip(raw_card_data, ":")
    card_number = get_card_number(raw_card_number)
    winning_numbers, card_numbers = get_numbers(raw_number_data)
    matching_numbers = get_matching_numbers(card_numbers, winning_numbers)
    points = __get_points(matching_numbers)
    logger.info(f'Card: {card_number}, points won: {points}, matching numbers: {matching_numbers}')
    return points


def __get_points(matching_numbers):
    if len(matching_numbers) > 0:
        return 2 ** (len(matching_numbers) - 1)
    else:
        return 0


if __name__ == '__main__':
    result = calculate_from_file("day4-data.txt")
    logger.warning(f'The solution for Day 4 is: {result}')
