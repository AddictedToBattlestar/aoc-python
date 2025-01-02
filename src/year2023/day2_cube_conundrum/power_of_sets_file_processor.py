import logging

from src.year2023.day2_cube_conundrum.power_of_sets_game_tracker import PowerOfSetsGameTracker

logger = logging.getLogger(__name__)


def process_file_for_power_of_sets(file_name):
    with open(file_name, "r") as text_file:
        lines = text_file.readlines()
        game_tracker = PowerOfSetsGameTracker()
        for line in lines:
            game_tracker.process_power_of_sets(line)
    return game_tracker.sum_of_power


if __name__ == '__main__':
    result = process_file_for_power_of_sets(file_name="day2-data.txt")
    logger.warning(f'The solution for Day 1 is: {result}')
