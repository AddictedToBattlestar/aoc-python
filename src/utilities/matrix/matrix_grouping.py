from typing import Dict

from src.utilities.matrix.matrix_coordinate import MatrixCoordinate


class MatrixGrouping:
    def __init__(self, identifier: str):
        self.identifier = identifier
        self.locations: list[MatrixCoordinate] = []

    def add_location(self, location: MatrixCoordinate):
        self.locations.append(location)

    @staticmethod
    def is_adjacent(location: MatrixCoordinate, other_location: MatrixCoordinate) -> bool:
        #above
        if other_location.x == location.x and other_location.y == location.y + 1:
            return True

        #below
        if other_location.x == location.x and other_location.y == location.y - 1:
            return True

        # left
        if other_location.x == location.x + 1 and other_location.y == location.y:
            return True

        # right
        if other_location.x == location.x - 1 and other_location.y == location.y:
            return True

        return False

    def segregate(self) -> Dict[int, list[MatrixCoordinate]]:
        current_group_id = 0
        location_groups = {current_group_id: self.locations}

        current_group = location_groups[current_group_id]
        next_group = []
        for location in location_groups[current_group_id]:
            if not self.is_adjacent_to_group(location, location_groups[current_group_id]):
                current_group.remove(location)
                next_group.append(location)
        if len(next_group) > 0:
            location_groups[current_group_id + 1] = next_group

        return location_groups

    def is_adjacent_to_group(self, location: MatrixCoordinate, location_list: list[MatrixCoordinate]) -> bool:
        for other_location in location_list:
            if self.is_adjacent(location, other_location):
                return True
        return False

