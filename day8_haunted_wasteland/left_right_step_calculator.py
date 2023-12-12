from day8_haunted_wasteland.file_reader import read_file
from typing import Optional


def calculate(network: dict,
              instructions: str,
              starting_location_id: str,
              target_location_id: Optional[str] = None) -> int:
    current_location = network[starting_location_id]
    current_location_id = starting_location_id
    steps_taken = 0
    target_found = False
    while not target_found:
        for direction in instructions:
            next_location_id = current_location[0] if direction == "L" else current_location[1]
            steps_taken += 1
            print(
                f"At location {current_location_id}, taking step number {steps_taken} going {direction} to location {next_location_id}.")
            if is_at_target_location(next_location_id, target_location_id):
                print(f"The {next_location_id} target location has been reached")
                return steps_taken
            else:
                current_location_id = next_location_id
                current_location = network[current_location_id]
    return steps_taken


def is_at_target_location(current_location_id, target_location: Optional[str] = None) -> bool:
    if target_location is None:
        if current_location_id[-1] == "Z":
            return True
    else:
        if current_location_id == target_location:
            return True
    return False


def calculate_from_file(file_name: str,
                        starting_location_id: str,
                        target_location_id: str) -> int:
    instructions, network_mapper = read_file(file_name)
    return calculate(network=network_mapper.network,
                     instructions=instructions,
                     starting_location_id=starting_location_id,
                     target_location_id=target_location_id)


if __name__ == '__main__':
    result = calculate_from_file(file_name="day8_data.txt",
                                 starting_location="AAA",
                                 target_location="ZZZ")
    print(f'The solution for Day 8 is: {result}')
