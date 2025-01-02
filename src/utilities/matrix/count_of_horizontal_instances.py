def count_of_horizontal_instances(input_data: list[str], string_to_match: str) -> int:
    if len(input_data) == 1 and len(input_data[0]) == 1:
        return 1 if input_data[0] == string_to_match else 0
    total_count = 0
    for input_line in input_data:
        total_count += input_line.count(string_to_match)
        total_count += input_line.count(string_to_match[::-1])
    return total_count
