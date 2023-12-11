import string

from day8_haunted_wasteland.network_mapper import NetworkMapper


def calculate(network: dict,
              instructions: string,
              starting_location: string,
              target_location: string) -> int:
    current_location = network[starting_location]
    current_location_id = starting_location
    steps_taken = 0
    target_found = False
    while not target_found:
        for direction in instructions:
            next_location_id = current_location[0] if direction == "L" else current_location[1]
            steps_taken += 1
            print(
                f"At location {current_location_id}, taking step number {steps_taken} going {direction} to location {next_location_id}.")
            if next_location_id == target_location:
                print(f"The {target_location} target location has been reached")
                return steps_taken
            else:
                current_location_id = next_location_id
                current_location = network[current_location_id]
    return steps_taken


def calculate_from_file(file_name: string,
                        starting_location: string,
                        target_location: string) -> int:
    with open(file_name, "r") as text_file:
        line_number = 1
        instructions = None
        lines = text_file.readlines()
        network_mapper = NetworkMapper()
        for line in lines:
            if line_number == 1:
                instructions = line.strip()
            else:
                if line_number > 2:
                    network_mapper.add_node(line)
            line_number += 1
        return calculate(network=network_mapper.network,
                         instructions=instructions,
                         starting_location=starting_location,
                         target_location=target_location)


if __name__ == '__main__':
    result = calculate_from_file(file_name="day8_data.txt",
                                 starting_location="AAA",
                                 target_location="ZZZ")
    print(f'The solution for Day 8 is: {result}')