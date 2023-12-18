from typing import Optional

from utilities.split_strip_to_int import split_strip_to_int


def get_values(raw_data):
    raw_value_data = raw_data.split(":")[1]
    return split_strip_to_int(raw_value_data, " ")


def get_min_button_time(total_time_allowed=7, minimum_distance=9) -> Optional[int]:
    for button_time in range(1, total_time_allowed - 1):
        distance_travelled = button_time * (total_time_allowed - button_time)
        if distance_travelled > minimum_distance:
            return button_time
    return None


def get_max_button_time(total_time_allowed=7, minimum_distance=9) -> Optional[int]:
    for button_time in reversed(range(1, total_time_allowed - 1)):
        distance_travelled = button_time * (total_time_allowed - button_time)
        if distance_travelled > minimum_distance:
            return button_time
    return None


def get_number_of_ways_to_win(total_time_allowed, minimum_distance):
    max_button_time = get_max_button_time(total_time_allowed, minimum_distance)
    min_button_time = get_min_button_time(total_time_allowed, minimum_distance)
    result = max_button_time - min_button_time + 1
    print(
        f"Total time allowed: {total_time_allowed}, minimum distance: {minimum_distance}. Button time - min:{min_button_time}, max:{max_button_time}, number of ways to win: {result}")
    return result


def get_total_number_of_ways_to_win(total_times_allowed, minimum_distances):
    total_number_of_ways_to_win = 1
    for i in range(0, len(total_times_allowed)):
        total_number_of_ways_to_win *= get_number_of_ways_to_win(total_times_allowed[i], minimum_distances[i])
    return total_number_of_ways_to_win


def get_total_number_of_ways_to_win_from_file(file_name):
    with open(file_name, "r") as text_file:
        total_times_allowed = get_values(text_file.readline())
        minimum_distances = get_values(text_file.readline())
        return get_total_number_of_ways_to_win(total_times_allowed, minimum_distances)


if __name__ == '__main__':
    result = get_total_number_of_ways_to_win_from_file(file_name="day6_data.txt")
    print(f"The total number of ways you could beat the record in each race is {result}")
