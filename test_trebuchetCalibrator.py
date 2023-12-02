from unittest import TestCase
from trebuchetCalibrator import get_calibration_value, calculate, calculate_from_file


class TestTrebuchetCalibrator(TestCase):
    def test_get_value(self):
        self.assertEqual(12, get_calibration_value(line="1abc2"))
        self.assertEqual(38, get_calibration_value(line="pqr3stu8vwx"))
        self.assertEqual(15, get_calibration_value(line="a1b2c3d4e5f"))
        self.assertEqual(77, get_calibration_value(line="treb7uchet"))

    def test_get_value_with_numbers_spelled(self):
        self.assertEqual(29, get_calibration_value(line="two1nine"))
        self.assertEqual(83, get_calibration_value(line="eightwothree"))
        self.assertEqual(13, get_calibration_value(line="abcone2threexyz"))
        self.assertEqual(24, get_calibration_value(line="xtwone3four"))
        self.assertEqual(42, get_calibration_value(line="4nineeightseven2"))
        self.assertEqual(14, get_calibration_value(line="zoneight234"))
        self.assertEqual(76, get_calibration_value(line="7pqrstsixteen"))

    def test_calculate(self):
        self.assertEqual(142, calculate(lines=[
            "1abc2",
            "pqr3stu8vwx",
            "a1b2c3d4e5f",
            "treb7uchet"
        ]))

    def test_calculate_from_file(self):
        self.assertEqual(142, calculate_from_file(file_name="day1-part1-sample-data.txt"))

    def test_calculate_from_file_part2(self):
        self.assertEqual(281, calculate_from_file(file_name="day1-part2-sample-data.txt"))