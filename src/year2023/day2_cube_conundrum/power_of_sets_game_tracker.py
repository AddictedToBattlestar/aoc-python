from src.year2023.day2_cube_conundrum.game_contents import GameContents


class PowerOfSetsGameTracker:
    def __init__(self):
        self.sum_of_power = 0

    def process_power_of_sets(self, game_data):
        game_contents = GameContents(game_data)
        power = game_contents.highest_red_count * game_contents.highest_green_count * game_contents.highest_blue_count
        self.sum_of_power += power
        return power, self.sum_of_power
