from day3_gear_ratios.grid_processor import GridProcessor


def process_file_for_sum_of_part_numbers(file_name):
    with open(file_name, "r") as text_file:
        lines = text_file.readlines()
        grid_processor = GridProcessor(lines)
        return grid_processor.sum_of_part_numbers


if __name__ == '__main__':
    result = process_file_for_sum_of_part_numbers(file_name="day3-data.txt")
    print(f'The solution for Day 3 is: {result}')
    # day 1 555475, too high
    # day 1 548370, too high