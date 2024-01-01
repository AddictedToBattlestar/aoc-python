import logging

from src.day2_cube_conundrum.bag_contents import BagContents
from src.day2_cube_conundrum.game_contents import GameContents

logger = logging.getLogger(__name__)


class SumOfGameTracker:
    def __init__(self, bag_contents: BagContents):
        self.sum_of_games_possible = 0
        self.bag_contents = bag_contents

    def process_sum_of_games_possible(self, game_data):
        game_contents = GameContents(game_data)
        if self.bag_contents.red_count >= game_contents.highest_red_count:
            if self.bag_contents.blue_count >= game_contents.highest_blue_count:
                if self.bag_contents.green_count >= game_contents.highest_green_count:
                    logger.info(f'Game {game_contents.id} was possible with the contents in the bag')
                    self.sum_of_games_possible += game_contents.id
                else:
                    logger.info(f'Game {game_contents.id} was NOT possible with the contents in the bag as there were not '
                          f'enough green cubes ({game_contents.highest_green_count} in game > {self.bag_contents.green_count} available)')
            else:
                logger.info(f'Game {game_contents.id} was NOT possible with the contents in the bag as there were not enough '
                      f'blue cubes ({game_contents.highest_blue_count} in game > {self.bag_contents.blue_count} available)')
        else:
            logger.info(f'Game {game_contents.id} was NOT possible with the contents in the bag as there were not enough red '
                  f'cubes ({game_contents.highest_red_count} in game > {self.bag_contents.red_count} available)')
        logger.info(f'Sum of games possible: {self.sum_of_games_possible}')
        return self.sum_of_games_possible
