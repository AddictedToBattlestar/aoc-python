import array
from curses.ascii import isdigit

from src.year2023.day3_gear_ratios.grid_part_number import GridPartNumber
from src.year2023.day3_gear_ratios.grid_symbol import GridSymbol


class GridProcessor():
    def __init__(self, lines: array):
        self.part_numbers_found = []
        self.current_part_number = GridPartNumber()
        self.symbols_found = []
        self.locate_part_numbers(lines)
        self.remove_part_numbers_not_symbol_adjacent()
        self.sum_of_part_numbers = GridProcessor.calculate_the_sum_of_part_numbers(self.part_numbers_found)

    def locate_part_numbers(self, lines: array):
        current_y_location = 0
        for line in lines:
            current_x_location = 0
            self.append_new_part_number_if_needed()
            for i in line:
                if isdigit(i):
                    self.current_part_number.expand_part_number(i, [current_x_location, current_y_location])
                else:
                    self.append_new_part_number_if_needed()
                    if i != ".":
                        self.symbols_found.append(GridSymbol(i, [current_x_location, current_y_location]))
                current_x_location += 1
            current_y_location -= 1
        self.append_new_part_number_if_needed()

    def append_new_part_number_if_needed(self):
        if self.current_part_number.part_number > 0:
            self.part_numbers_found.append(self.current_part_number)
            self.current_part_number = GridPartNumber()

    def remove_part_numbers_not_symbol_adjacent(self):
        part_numbers_to_keep = []
        for part_number in self.part_numbers_found:
            if self.is_part_number_adjacent_to_symbol(part_number):
                part_numbers_to_keep.append(part_number)
        self.part_numbers_found = part_numbers_to_keep
    def is_part_number_adjacent_to_symbol(self, part_number: GridPartNumber):
        for point in part_number.coordinates:
            if self.is_point_adjacent_to_symbol(point):
                return True
        return False

    def is_point_adjacent_to_symbol(self, point: array):
        x_coordinate = point[0]
        y_coordinate = point[1]

        if self.is_symbol_present(x_coordinate - 1, y_coordinate + 1):
            return True
        if self.is_symbol_present(x_coordinate, y_coordinate + 1):
            return True
        if self.is_symbol_present(x_coordinate + 1, y_coordinate + 1):
            return True

        if self.is_symbol_present(x_coordinate - 1, y_coordinate):
            return True
        if self.is_symbol_present(x_coordinate, y_coordinate):
            return True
        if self.is_symbol_present(x_coordinate + 1, y_coordinate):
            return True

        if self.is_symbol_present(x_coordinate - 1, y_coordinate - 1):
            return True
        if self.is_symbol_present(x_coordinate, y_coordinate - 1):
            return True
        if self.is_symbol_present(x_coordinate + 1, y_coordinate - 1):
            return True

    def is_symbol_present(self, x_coordinate, y_coordinate):
        for grid_symbol in self.symbols_found:
            if grid_symbol.coordinate == [x_coordinate, y_coordinate]:
                return True
        return False

    @staticmethod
    def calculate_the_sum_of_part_numbers(grid_part_numbers):
        sum_of_part_numbers = 0
        for grid_part_number in grid_part_numbers:
            sum_of_part_numbers += grid_part_number.part_number
        return sum_of_part_numbers
