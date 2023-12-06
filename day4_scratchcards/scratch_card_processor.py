from utilities.split_strip import split_strip
from utilities.split_strip_to_int import split_strip_to_int


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
    card_number = __get_card_number(raw_card_number)
    winning_numbers, card_numbers = __get_numbers(raw_number_data)
    matching_numbers = __get_matching_numbers(card_numbers, winning_numbers)
    points = __get_points(matching_numbers)
    print(f'Card: {card_number}, points won: {points}, matching numbers: {matching_numbers}')
    return points


def __get_points(matching_numbers):
    if len(matching_numbers) > 0:
        return 2 ** (len(matching_numbers) - 1)
    else:
        return 0


def __get_matching_numbers(card_numbers, winning_numbers):
    matching_numbers = []
    for number in card_numbers:
        if number in winning_numbers:
            matching_numbers.append(number)
    return matching_numbers


def __get_numbers(raw_number_data):
    raw_winning_numbers, raw_card_numbers = split_strip(raw_number_data, "|")
    winning_numbers = split_strip_to_int(raw_winning_numbers, " ")
    card_numbers = split_strip_to_int(raw_card_numbers, " ")
    return winning_numbers, card_numbers


def __get_card_number(raw_card_number) -> int:
    split_data = split_strip(raw_card_number, " ")
    return int(split_data[-1])


if __name__ == '__main__':
    result = calculate_from_file("day4-data.txt")
    print(f'The solution for Day 4 is: {result}')