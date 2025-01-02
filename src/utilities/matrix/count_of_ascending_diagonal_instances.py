from src.utilities.matrix.count_of_horizontal_instances import count_of_horizontal_instances


def count_of_ascending_diagonal_instances(input_data: list[str], string_to_match: str) -> int:
    if len(input_data) == 1 and len(input_data[0]) == 1:
        return 1 if input_data[0] == string_to_match else 0
    rows_to_scan = []
    for input_character in input_data[0]:
        rows_to_scan.append(input_character)
    row_offset = 1
    for input_line in input_data[1:]:
        for x_index, input_character in enumerate(input_line):
            if len(rows_to_scan) > x_index + row_offset:
                rows_to_scan[x_index + row_offset] = input_character + rows_to_scan[x_index + row_offset]
            else:
                rows_to_scan.append(input_character)
        row_offset += 1
    return count_of_horizontal_instances(rows_to_scan, string_to_match)