import src.year2024.day3.mull_it_over as mull
import pytest

from src.settings import PROJECT_ROOT

@pytest.mark.parametrize("test_input, pattern_to_match, expected", [
    ("012345mul(123,456)12345", mull.multiplier_regex, 6),
    ("0123456789mul(123,456)12345", mull.multiplier_regex, 10),
    ("no-matches-here", mull.multiplier_regex, None),
    ("012345do()12345", mull.do_regex, 6),
    ("0123456789do()12345", mull.do_regex, 10),
    ("no-matches-here", mull.do_regex, None),
    ("012345don't()12345", mull.dont_regex, 6),
    ("0123456789don't()12345", mull.dont_regex, 10),
    ("no-matches-here", mull.dont_regex, None),
])
def test_find_next_multiplier_position(test_input, pattern_to_match, expected):
    result = mull.MullItOverProcessor.find_next_position(test_input, pattern_to_match)

    assert result == expected

def test_find_enabled_multiplier_sections():
    #                                       |-do --------------|--don't------------------------------------|-do-----|
    mull_it_over_processor = mull.MullItOverProcessor("xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))")
    result = mull_it_over_processor.enabled_multiplier_sections

    assert result == ["xmul(2,4)&mul[3,7]!^", "?mul(8,5))"]


def test_find_multipliers():
    result = mull.find_multipliers("xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))")

    assert len(result) == 4
    assert "mul(2,4)" in result
    assert "mul(5,5)" in result
    assert "mul(11,8)" in result
    assert "mul(8,5)" in result

@pytest.mark.parametrize("test_input,expected", [("mul(2,4)", [2, 4]), ("mul(11,8)", [11,8])])
def test_parse_numbers_to_multiply(test_input, expected):
    result = mull.parse_numbers_to_multiply(test_input)

    assert result == expected

def test_parse_multipliers():
    result = mull.parse_multipliers("xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))")

    assert len(result) == 4
    assert result[0] == [2, 4]
    assert result[1] == [5, 5]
    assert result[2] == [11, 8]
    assert result[3] == [8, 5]

def test_add_it_up_part1():
    result = mull.add_it_up("xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))", False)

    assert result == 161

def test_add_it_up_from_file_part1():
    result = mull.add_it_up_from_file(PROJECT_ROOT + "/year2024/day3/data_sample_part1.txt", False)

    assert result == 161

def test_add_it_up_part2():
    result = mull.add_it_up("xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))", True)

    assert result == 48

def test_add_it_up_from_file_part2():
    result = mull.add_it_up_from_file(PROJECT_ROOT + "/year2024/day3/data_sample_part2.txt", True)

    assert result == 48