import array

from src.day8_haunted_wasteland.file_reader import read_file
from src.day8_haunted_wasteland.network_mapper import NetworkMapper
from src.day8_haunted_wasteland.left_right_step_calculator import calculate as left_right_step_calculator


def calculate_from_file(file_name: str):
    instructions, network_mapper = read_file(file_name)
    return calculate(instructions, network_mapper)


def calculate(instructions: str, network_mapper: NetworkMapper) -> int:
    possible_network_paths = {}
    for starting_location_id in network_mapper.starting_node_ids:
        number_of_steps, location_id_reached = left_right_step_calculator(network=network_mapper.network,
                                                                          instructions=instructions,
                                                                          starting_location_id=starting_location_id)
        possible_network_paths[starting_location_id] = (number_of_steps, location_id_reached)
    for starting_location_id in network_mapper.terminating_node_ids:
        number_of_steps, location_id_reached = left_right_step_calculator(network=network_mapper.network,
                                                                          instructions=instructions,
                                                                          starting_location_id=starting_location_id)
        possible_network_paths[starting_location_id] = (number_of_steps, location_id_reached)

    return calculate_in_parallel(network_mapper.starting_node_ids, possible_network_paths)


def calculate_in_parallel(starting_location_ids: array, possible_network_paths: dict) -> int:
    print(f"Calculating steps in parallel.  Starting at locations: {starting_location_ids}")
    step_trackers, current_count_of_steps = setup_step_tracking(starting_location_ids, possible_network_paths)
    are_steps_in_sync = False
    while not are_steps_in_sync:
        print(f"Current count of steps taken: {current_count_of_steps}")
        are_steps_in_sync = True
        for step_tracker in step_trackers:
            if step_tracker.steps_taken < current_count_of_steps:
                are_steps_in_sync = False
                number_of_steps_taken, location_id_reached = possible_network_paths[step_tracker.current_location_id]
                step_tracker.take_step(number_of_steps_taken, location_id_reached)
                if current_count_of_steps < step_tracker.steps_taken:
                    current_count_of_steps = step_tracker.steps_taken

    print(f"Steps taken are in sync for the separate paths taken: {current_count_of_steps}")
    return current_count_of_steps


def setup_step_tracking(current_location_ids, possible_network_paths: dict):
    step_trackers = []
    current_count_of_steps = 0
    for current_location_id in current_location_ids:
        number_of_steps_taken, next_location_id = possible_network_paths[current_location_id]
        step_trackers.append(StepTracker(current_location_id, next_location_id, number_of_steps_taken))
        if number_of_steps_taken > current_count_of_steps:
            current_count_of_steps = number_of_steps_taken
    return step_trackers, current_count_of_steps


def print_taking_step(current_location_id: str, new_location_id: str, steps_taken: int):
    print(f"Taking step: {current_location_id}->{new_location_id}, steps taken: {steps_taken}")


class StepTracker:
    def __init__(self, starting_location_id: str, current_location_id: str, steps_taken: int):
        print_taking_step(starting_location_id, current_location_id, steps_taken)
        self.starting_location_id = starting_location_id
        self.current_location_id = current_location_id
        self.steps_taken = steps_taken

    def take_step(self, steps_taken: int, new_location_id: str):
        print_taking_step(self.current_location_id, new_location_id, steps_taken)
        self.steps_taken += steps_taken
        self.current_location_id = new_location_id


if __name__ == '__main__':
    result = calculate_from_file(file_name="day8_data.txt")
    print(f'The solution for Day 8 is: {result}')
