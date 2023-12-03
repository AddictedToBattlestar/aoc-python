from day2_cube_conundrum.bag_contents import BagContents
from day2_cube_conundrum.game_tracker import GameTracker


def process_file(file_name, bag_contents: BagContents):
    with open(file_name, "r") as text_file:
        lines = text_file.readlines()
        game_tracker = GameTracker(bag_contents)
        for line in lines:
            running_total = game_tracker.process_game(line)
    return game_tracker.sum_of_games_possible


if __name__ == '__main__':
    bag_contents = BagContents(12, 13, 14)
    result = process_file(file_name="day2-data.txt", bag_contents=bag_contents)
    print(f'The solution for Day 1 is: {result}')
    # part 1: 1848 too low