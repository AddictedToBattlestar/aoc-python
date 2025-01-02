from enum import Enum
from typing import List

from src.utilities.file_reader import read_lines_from_file

class ReportDirection(Enum):
    INCREASING = 0
    DECREASING = 1

def get_count_of_safe_reports(input_data: List[str], use_dampener: bool) -> int:
    count_of_safe_reports = 0
    for report_line in input_data:
        if is_report_line_safe(report_line, use_dampener):
            print(f"{report_line}: Safe")
            count_of_safe_reports += 1
        else:
            print(f"{report_line}: Unsafe")
    return count_of_safe_reports

def is_report_line_safe(report_line: str, use_dampener: bool) -> bool:
    report_levels = [int(x) for x in report_line.split(' ')]
    if is_report_safe(report_levels):
        return True
    else:
        if use_dampener and is_there_a_shortened_report_that_is_safe(report_levels):
            return True
        else:
            return False

def is_report_safe(report_levels: List[int]) -> bool:
    direction = ReportDirection.DECREASING if report_levels[0] > report_levels[-1] else ReportDirection.INCREASING
    previous_level = report_levels[0]
    if not is_first_level_safe(report_levels):
        return False
    for index, current_level in enumerate(report_levels[1:]):
        if is_level_safe(direction, previous_level, current_level):
            previous_level = current_level
        else:
            return False
    return True

def is_there_a_shortened_report_that_is_safe(report_levels: List[int]) -> bool:
    for index, value in enumerate(report_levels):
        revised_report_levels = report_levels[:]
        del revised_report_levels[index]
        if is_report_safe(revised_report_levels):
            return True
    return False

def is_first_level_safe(report_levels: List[int]) -> bool:
    direction_of_2nd_and_3rd_levels = ReportDirection.DECREASING if report_levels[1] > report_levels[2] else ReportDirection.INCREASING
    return is_level_safe(direction_of_2nd_and_3rd_levels, report_levels[0], report_levels[1])

def is_level_safe(direction: ReportDirection, previous_level: int, current_level: int) -> bool:
    if abs(previous_level - current_level) < 1 or 3 < abs(previous_level - current_level):
        return False
    if direction == ReportDirection.INCREASING and previous_level > current_level:
        return False
    elif direction == ReportDirection.DECREASING and previous_level < current_level:
        return False
    else:
        return True

def get_count_of_safe_reports_from_file(file_name: str, use_dampener: bool):
    input_data = read_lines_from_file(file_name)
    return get_count_of_safe_reports(input_data, use_dampener)

if __name__ == '__main__':
    part1_result = get_count_of_safe_reports_from_file('data.txt', False)
    print(f"day2 part 1 result: {part1_result}")
    part2_result = get_count_of_safe_reports_from_file('data.txt', True)
    print(f"day2 part 2 result: {part2_result}")