from utilities.split_strip import split_strip


class LeftRightStepCalculator:
    def __init__(self):
        self.network = {}

    def add_node(self, raw_node):
        location, paths_to_take = split_strip(raw_node, "=")
        paths_to_take = paths_to_take.replace(")", "").replace("(", "")
        left_path, right_path = split_strip(paths_to_take, ",")
        self.network[location] = (left_path, right_path)

    def add_nodes(self, raw_nodes):
        for raw_node in raw_nodes:
            self.add_node(raw_node)

    def calculate(self, instructions, starting_location, target_location):
        current_location = self.network[starting_location]
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
                    current_location = self.network[current_location_id]
        return steps_taken

    def calculate_from_file(self, file_name, starting_location, target_location):
        with open(file_name, "r") as text_file:
            line_number = 1
            instructions = None
            lines = text_file.readlines()
            for line in lines:
                if line_number == 1:
                    instructions = line.strip()
                else:
                    if line_number > 2:
                        self.add_node(line)
                line_number += 1
            return self.calculate(instructions, starting_location, target_location)


if __name__ == '__main__':
    subject = LeftRightStepCalculator()
    result = subject.calculate_from_file(file_name="day8_data.txt",
                                         starting_location="AAA",
                                         target_location="ZZZ")
    print(f'The solution for Day 8 is: {result}')
