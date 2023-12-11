import string
import array


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
                print(f"Direction taken {direction}, now at locations {current_location_ids}, steps taken: {steps_taken}")