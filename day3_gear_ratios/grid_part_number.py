import array
import string


class GridPartNumber:
    def __init__(self):
        self.part_number = 0
        self.coordinates = []

    def expand_part_number(self, additional_value: string, coordinate: array):
        self.part_number *= 10
        self.part_number += int(additional_value)
        self.coordinates.append(coordinate)
