from pickle import FALSE

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
    (MatrixCoordinate(1, 1), False),
    (MatrixCoordinate(2, 1), True),
    (MatrixCoordinate(3, 1), False),
    (MatrixCoordinate(4, 1), False),
    (MatrixCoordinate(5, 1), False),

    (MatrixCoordinate(1, 2), True),
    #
    (MatrixCoordinate(3, 2), True),
    (MatrixCoordinate(4, 2), True),
    (MatrixCoordinate(5, 2), False),

    (MatrixCoordinate(1, 3), False),
    (MatrixCoordinate(2, 3), True),
    (MatrixCoordinate(3, 3), True),
    #
    (MatrixCoordinate(5, 3), True),

    (MatrixCoordinate(1, 4), False),
    (MatrixCoordinate(2, 4), False),
    (MatrixCoordinate(3, 4), False),
    (MatrixCoordinate(4, 4), True),
    (MatrixCoordinate(5, 4), False)
])
def test_matrix_grouping_adjacent(test_location, expected):
    subject = MatrixGrouping("X")
    subject.add_location(MatrixCoordinate(2, 2))
    subject.add_location(MatrixCoordinate(4, 3))

    assert subject.is_adjacent(test_location) == expected
