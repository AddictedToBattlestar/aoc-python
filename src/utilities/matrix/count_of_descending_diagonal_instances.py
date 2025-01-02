from src.utilities.matrix.count_of_ascending_diagonal_instances import count_of_ascending_diagonal_instances
from src.utilities.matrix.rotate_matrix import rotate_matrix_clockwise_90_degrees


def count_of_descending_diagonal_instances(input_data: list[str], string_to_match: str) -> int:
    if input_data == [""]:
        return 0
    if len(input_data) == 1 and len(input_data[0]) == 1:
        return 1 if input_data[0] == string_to_match else 0
    rotated = rotate_matrix_clockwise_90_degrees(input_data)
    return count_of_ascending_diagonal_instances(rotated, string_to_match)