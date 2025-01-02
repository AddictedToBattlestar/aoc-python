from src.year2024.day4.ceres_search import word_search, word_search_from_file
from src.settings import PROJECT_ROOT


def test_part1_sample_data():
    sample_data = [
        "..X...",
        ".SAMX.",
        ".A..A.",
        "XMAS.S",
        ".X....",
    ]

    result = word_search(sample_data, "XMAS")

    assert result == 4

def test_part1_small_sample_data_from_file():
    result = word_search_from_file(PROJECT_ROOT + "/year2024/day4/data_sample_small.txt", "XMAS")

    assert result == 4

def test_part1_sample_data_from_file():
    result = word_search_from_file(PROJECT_ROOT + "/year2024/day4/data_sample.txt", "XMAS")

    assert result == 18