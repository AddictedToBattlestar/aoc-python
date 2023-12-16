from typing import Optional

from utilities.split_strip import split_strip
from utilities.split_strip_to_int import split_strip_to_int


class SeedingMap:
    def __init__(self, raw_seeding_map):
        values = split_strip_to_int(raw_seeding_map, " ")
        self.min = values[1]
        self.max = self.min + values[2] - 1
        self.offset = values[0] - values[1]


class SeedingLocationMapper:
    def __init__(self, raw_seeding_map_lines, name: Optional[str] = None):
        self.seeding_map = []
        self.name = name
        for raw_seeding_map in raw_seeding_map_lines:
            self.seeding_map.append(SeedingMap(raw_seeding_map))

    def get_destination_location(self, source_location: int) -> int:
        destination_location = source_location
        for seeding_map in self.seeding_map:
            if seeding_map.min <= source_location <= seeding_map.max:
                destination_location = source_location + seeding_map.offset
                break
        if self.name is not None:
            print(f"{self.name} maps {source_location} to {destination_location}")
        return destination_location


def find_seed_numbers(raw_seed_numbers, use_revised_seeding_map: Optional[bool] = False):
    seed_values = split_strip_to_int(raw_seed_numbers, " ")
    if not use_revised_seeding_map:
        return seed_values

    seed_numbers = []
    current_seed_number = None
    for seed_value_index, seed_value in enumerate(seed_values):
        if seed_value_index % 2 == 0:
            current_seed_number = seed_value
            seed_numbers.append(seed_value)
        else:
            for _ in range(seed_value - 1):
                current_seed_number += 1
                seed_numbers.append(current_seed_number)
    return seed_numbers


class SeedingCategoryProcessor:
    def __init__(self, seeding_mappers):
        self.seeding_mappers = seeding_mappers

    def find_location_number(self, seed_number):
        current_mapped_value = seed_number
        for seeding_map in self.seeding_mappers:
            current_mapped_value = seeding_map.get_destination_location(current_mapped_value)
        return current_mapped_value

    def find_lowest_location_number(self, raw_seed_numbers, use_revised_seeding_map: Optional[bool] = False):
        seed_numbers = find_seed_numbers(raw_seed_numbers, use_revised_seeding_map)
        lowest_location_number = None
        for seed_number in seed_numbers:
            location_number = self.find_location_number(seed_number)
            if lowest_location_number is None or lowest_location_number > location_number:
                lowest_location_number = location_number
        return lowest_location_number


def calculate_from_file(file_name, use_revised_seeding_map: Optional[bool] = False):
    with open(file_name, "r") as text_file:
        lines = text_file.readlines()

        ignore, raw_seed_numbers = split_strip(lines[0], ":")

        seeding_mappers = []
        current_line_number = 2

        while len(lines) > current_line_number:
            map_name, ignore = split_strip(lines[current_line_number], " ")
            current_line_number += 1
            raw_seeding_map_lines = []
            while len(lines) > current_line_number and lines[current_line_number].strip() != "":
                raw_seeding_map_lines.append(lines[current_line_number])
                current_line_number += 1
            new_mapper = SeedingLocationMapper(raw_seeding_map_lines, map_name)
            seeding_mappers.append(new_mapper)
            current_line_number += 1

        processor = SeedingCategoryProcessor(seeding_mappers)

        return processor.find_lowest_location_number(raw_seed_numbers, use_revised_seeding_map)


if __name__ == '__main__':
    result = calculate_from_file(file_name="day5_data.txt", use_revised_seeding_map=True)
    print(f"The lowest location number found for the initial seed numbers is {result}")
