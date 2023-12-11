import string
import array

from day8_haunted_wasteland.network_mapper import NetworkMapper


def calculate(starting_location_ids: array,
              network: dict,
              instructions: string) -> int:
    current_location_ids = starting_location_ids
    print(f"Starting at locations: {current_location_ids}")
    steps_taken = 0
    while True:
        for direction in instructions:
            target_found = True
            next_location_ids = []
            for location_id in current_location_ids:
                location = network[location_id]
                next_location_id = location[0] if direction == "L" else location[1]
                next_location_ids.append(next_location_id)
                if next_location_id[-1] != "Z" and target_found:
                    target_found = False
            current_location_ids = next_location_ids
            steps_taken += 1
            if target_found:
                print(f"The target locations have been reached: {current_location_ids}, steps taken: {steps_taken}")
                return steps_taken
            else:
                print(
                    f"Direction taken {direction}, now at locations {current_location_ids}, steps taken: {steps_taken}")


def calculate_from_file(file_name: string) -> int:
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
        return calculate(starting_location_ids=network_mapper.starting_node_ids,
                         network=network_mapper.network,
                         instructions=instructions)

if __name__ == '__main__':
    result = calculate_from_file(file_name="day8_data.txt")
    print(f'The solution for Day 8 is: {result}')
