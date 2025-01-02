from src.utilities.file_reader import read_lines_from_file
from src.utilities.matrix.count_of_ascending_diagonal_instances import count_of_ascending_diagonal_instances
from src.utilities.matrix.count_of_descending_diagonal_instances import count_of_descending_diagonal_instances
from src.utilities.matrix.count_of_horizontal_instances import count_of_horizontal_instances
from src.utilities.matrix.count_of_vertical_instances import count_of_vertical_instances


def word_search(input_data: list[str], word: str) -> int:
    total_count = 0
    total_count += count_of_horizontal_instances(input_data, word)
    total_count += count_of_vertical_instances(input_data, word)
    total_count += count_of_descending_diagonal_instances(input_data, word)
    total_count += count_of_ascending_diagonal_instances(input_data, word)
    return total_count

def word_search_from_file(file_name, word):
    input_data = read_lines_from_file(file_name)
    return word_search(input_data, word)

if __name__ == "__main__":
    part1_result = word_search_from_file("data.txt", "XMAS")
    print(f"Part 1 result: {part1_result}")