from typing import Dict

from src.utilities.matrix.matrix_coordinate import MatrixCoordinate


class MatrixGrouping:
    def __init__(self, identifier: str):
        self.identifier = identifier
        self.locations: list[MatrixCoordinate] = []

    def add_location(self, location: MatrixCoordinate):
        self.locations.append(location)

    def is_adjacent(self, location: MatrixCoordinate) -> bool:
        for group_location in self.locations:
            #above
            if group_location.x == location.x and group_location.y == location.y + 1:
                return True

            #below
            if group_location.x == location.x and group_location.y == location.y - 1:
                return True

            # left
            if group_location.x == location.x + 1 and group_location.y == location.y:
                return True

            # right
            if group_location.x == location.x - 1 and group_location.y == location.y:
                return True
        return False

    def segregate(self) -> Dict[int, list[MatrixCoordinate]]:
        return {0: self.locations}
