import re

from src.utilities.file_reader import read_lines_from_file

multiplier_regex = r"mul[(][0-9]{1,3}[,][0-9]{1,3}[)]"
do_regex = r"do[(][)]"
do_length = 4
dont_regex = r"don't[(][)]"
dont_length = 7

class MullItOverProcessor:
    def __init__(self, input_string: str):
        self.input_string: str = input_string
        self.enabled_multiplier_sections: list[str] = []
        self.build_multiplier_sections()

    def build_multiplier_sections(self):
        while self.input_string is not None:
            self.process_input_string_for_next_multiplier_section()

    def process_input_string_for_next_multiplier_section(self):
        end_of_multiplier_section = self.find_next_position(self.input_string, dont_regex)
        new_multiplier_section = self.input_string[:end_of_multiplier_section]
        self.enabled_multiplier_sections.append(new_multiplier_section)

        if end_of_multiplier_section is None:
            self.input_string = None
        else:
            self.input_string = self.input_string[end_of_multiplier_section + dont_length:]
            start_of_next_multiplier_section = self.find_next_position(self.input_string, do_regex)
            if start_of_next_multiplier_section is None:
                self.input_string = None
            else:
                self.input_string = self.input_string[start_of_next_multiplier_section + do_length:]

    @staticmethod
    def find_next_position(input_string: str, pattern_to_match: str) -> int:
        match = re.search(pattern_to_match, input_string)
        return match.start() if match else None

def find_multipliers(input_string: str) -> list[str]:
    match = re.findall(multiplier_regex, input_string)
    return match

def parse_numbers_to_multiply(multiplier_as_string: str) -> list[int]:
    return [int(x) for x in multiplier_as_string[4:-1].split(",")]

def parse_multipliers(input_string: str) -> list[list[int]]:
    multipliers = find_multipliers(input_string)
    results = []
    for multiplier in multipliers:
        results.append(parse_numbers_to_multiply(multiplier))
    return results

def add_it_up(input_string: str, enabled_multipliers_only: bool) -> int:
    if enabled_multipliers_only:
        mull_it_over_processor = MullItOverProcessor(input_string)
        input_string = ''.join(mull_it_over_processor.enabled_multiplier_sections)
    multipliers = parse_multipliers(input_string)
    result = 0
    for multiplier in multipliers:
        result += multiplier[0] * multiplier[1]
    return result

def add_it_up_from_file(file_name: str, enabled_multipliers_only: bool) -> int:
    input_data = read_lines_from_file(file_name)
    input_string = ''.join(input_data)
    return add_it_up(input_string, enabled_multipliers_only)

if __name__ == "__main__":
    # part_1_result = add_it_up_from_file("data.txt", False)
    # print(f"Part 1 result: {part_1_result}")
    part_2_result = add_it_up_from_file("data.txt", True)
    print(f"Part 2 result: {part_2_result}")
