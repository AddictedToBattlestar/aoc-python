from unittest import TestCase

from src.day3_gear_ratios.grid_part_number import GridPartNumber


class TestPartNumber(TestCase):
    def test_part_number(self):
        part_number = GridPartNumber()
        self.assertEqual(0, part_number.part_number)
        self.assertEqual([], part_number.coordinates)

    def test_expand_part_number(self):
        part_number = GridPartNumber()

        part_number.expand_part_number("1", [1])
        self.assertEqual(1, part_number.part_number)
        self.assertEqual([[1]], part_number.coordinates)

        part_number.expand_part_number("2", [2])
        self.assertEqual(12, part_number.part_number)
        self.assertEqual([[1],[2]], part_number.coordinates)

        part_number.expand_part_number("3", [3])
        self.assertEqual(123, part_number.part_number)
        self.assertEqual([[1],[2],[3]], part_number.coordinates)