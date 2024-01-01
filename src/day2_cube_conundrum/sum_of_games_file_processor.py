import logging

from src.day2_cube_conundrum.bag_contents import BagContents
from src.day2_cube_conundrum.sum_of_game_tracker import SumOfGameTracker

logger = logging.getLogger(__name__)

def process_file_for_sum_of_game(file_name, bag_contents: BagContents):
    with open(file_name, "r") as text_file:
        lines = text_file.readlines()
        game_tracker = SumOfGameTracker(bag_contents)
        for line in lines:
            game_tracker.process_sum_of_games_possible(line)
    return game_tracker.sum_of_games_possible


if __name__ == '__main__':
    bag_contents = BagContents(12, 13, 14)
    result = process_file_for_sum_of_game(file_name="day2-data.txt", bag_contents=bag_contents)
    logger.warning(f'The solution for Day 1 is: {result}')
    # part 1: 1848 too low