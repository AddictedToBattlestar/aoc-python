from unittest import TestCase
from trebuchetCalibrator import get_value, calculate, calculate_from_file


class TestTrebuchetCalibrator(TestCase):
    def test_get_value(self):
        self.assertEqual(12, get_value(line="1abc2"))
        self.assertEqual(38, get_value(line="pqr3stu8vwx"))
        self.assertEqual(15, get_value(line="a1b2c3d4e5f"))
        self.assertEqual(77, get_value(line="treb7uchet"))

    def test_calculate(self):
        self.assertEqual(142, calculate(lines=[
            "1abc2",
            "pqr3stu8vwx",
            "a1b2c3d4e5f",
            "treb7uchet"
        ]))

    def test_calculate_from_file(self):
        self.assertEqual(142, calculate_from_file(file_name="day1-part1-sample-data.txt"))