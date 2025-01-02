from src.year2024.day2.red_nosed_reports import get_count_of_safe_reports, get_count_of_safe_reports_from_file, is_report_line_safe
from src.settings import PROJECT_ROOT


def test_part1_sample_data():
    sample_data = [
        "7 6 4 2 1",
        "1 2 7 8 9",
        "9 7 6 2 1",
        "1 3 2 4 5",
        "8 6 4 4 1",
        "1 3 6 7 9"
    ]

    result = get_count_of_safe_reports(sample_data, False)

    assert result == 2

def test_part1_sample_data_from_file():
    result = get_count_of_safe_reports_from_file(PROJECT_ROOT + "/year2024/day2/data_sample.txt", False)

    assert result == 2

def test_part2_is_report_safe():
    report_line = "1 5 6 7 8"
    result = is_report_line_safe(report_line, True)

    assert result == True

def test_part2_is_report_safe_another_flaw():
    report_line = "1 3 2 4 5"
    result = is_report_line_safe(report_line, True)

    assert result == True

def test_part2_sample_data_from_file():
    result = get_count_of_safe_reports_from_file(PROJECT_ROOT + "/year2024/day2/data_sample.txt", True)

    assert result == 4