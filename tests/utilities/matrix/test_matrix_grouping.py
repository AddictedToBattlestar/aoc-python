from typing import Dict

import pytest

from src.utilities.matrix.matrix_coordinate import MatrixCoordinate
from src.utilities.matrix.matrix_grouping import MatrixGrouping


#  012345
# 0
# 1  T
# 2 TXTT
# 3  TTXT
# 4    T
@pytest.mark.parametrize("test_location, expected", [
    (MatrixCoordinate(1, 1, "X"), False),
    (MatrixCoordinate(2, 1, "X"), True),
    (MatrixCoordinate(3, 1, "X"), False),
    (MatrixCoordinate(4, 1, "X"), False),
    (MatrixCoordinate(5, 1, "X"), False),

    (MatrixCoordinate(1, 2, "X"), True),
    #
    (MatrixCoordinate(3, 2, "X"), True),
    (MatrixCoordinate(4, 2, "X"), True),
    (MatrixCoordinate(5, 2, "X"), False),

    (MatrixCoordinate(1, 3, "X"), False),
    (MatrixCoordinate(2, 3, "X"), True),
    (MatrixCoordinate(3, 3, "X"), True),
    #
    (MatrixCoordinate(5, 3, "X"), True),

    (MatrixCoordinate(1, 4, "X"), False),
    (MatrixCoordinate(2, 4, "X"), False),
    (MatrixCoordinate(3, 4, "X"), False),
    (MatrixCoordinate(4, 4, "X"), True),
    (MatrixCoordinate(5, 4, "X"), False)
])
def test_matrix_grouping_adjacent(test_location, expected):
    subject = MatrixGrouping("X")
    subject.add_location(MatrixCoordinate(2, 2, "X"))
    subject.add_location(MatrixCoordinate(4, 3, "X"))

    assert subject.is_adjacent(test_location) == expected


def fill_matrix_line(matrix_groups: Dict[str, MatrixGrouping], matrix_line_as_string: str, y_index: int):
    for x_index, matrix_character in enumerate(matrix_line_as_string):
        matching_matrix_group = matrix_groups[matrix_character]
        matching_matrix_group.add_location(MatrixCoordinate(x_index, y_index, matrix_character))

def test_addition():
    subject = {
        "X": MatrixGrouping("X"),
        "O": MatrixGrouping("O")
    }

    fill_matrix_line(subject, "XXXOO", 0)
    fill_matrix_line(subject, "XOXOO", 1)
    fill_matrix_line(subject, "XXXXX", 2)
    fill_matrix_line(subject, "OOXOX", 3)
    fill_matrix_line(subject, "OOXXX", 4)

    subject_X = subject["X"]
    assert len(subject_X.locations) == 15
    subject_O = subject["O"]
    assert len(subject_O.locations) == 10

def test_segregation():
    identifier_groups = {
        "X": MatrixGrouping("X"),
        "O": MatrixGrouping("O")
    }

    fill_matrix_line(identifier_groups, "XX", 0)
    fill_matrix_line(identifier_groups, "XO", 1)

    subject = identifier_groups["X"]
    result = subject.segregate()

    result_keys = list(result.keys())
    assert len(result_keys) == 1
    result_group = result.get(result_keys[0])
    result_group.sort()
    assert result_group == [
        MatrixCoordinate(0, 0, "X"),
        MatrixCoordinate(0, 1, "X"),
        MatrixCoordinate(1, 0, "X")
    ]

