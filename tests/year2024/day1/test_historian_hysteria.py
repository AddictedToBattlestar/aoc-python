import pytest
from src.year2024.day1.historian_hysteria import get_total_distance, get_total_distance_from_file, get_similarity_score, get_similarity_score_from_file
from src.settings import PROJECT_ROOT


def test_part_1_sample():
    sample_1_data = [
        "3   4",
        "4   3",
        "2   5",
        "1   3",
        "3   9",
        "3   3"
    ]
    assert get_total_distance(sample_1_data) == 11

def test_part_1_sample_file():
    assert get_total_distance_from_file(PROJECT_ROOT + "/year2024/day1/data_sample.txt") == 11

def test_part_2_sample():
    sample_1_data = [
        "3   4",
        "4   3",
        "2   5",
        "1   3",
        "3   9",
        "3   3"
    ]
    assert get_similarity_score(sample_1_data) == 31

def test_part_2_sample_file():
    assert get_similarity_score_from_file(PROJECT_ROOT + "/year2024/day1/data_sample.txt") == 31