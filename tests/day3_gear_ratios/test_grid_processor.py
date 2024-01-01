from unittest import TestCase

from src.day3_gear_ratios.grid_part_number import GridPartNumber
from src.day3_gear_ratios.grid_processor import GridProcessor


class Test(TestCase):
    def test_grid_process_test1(self):
        fake_grid = [
            "12*"
        ]

        subject = GridProcessor(fake_grid)

        self.assertEqual(1, len(subject.part_numbers_found))
        part_number_returned = subject.part_numbers_found[0]
        self.assertEqual(12, part_number_returned.part_number)
        self.assertEqual([[0, 0], [1, 0]], part_number_returned.coordinates)

        fake_grid = [
            ".12*"
        ]

        subject = GridProcessor(fake_grid)

        self.assertEqual(1, len(subject.part_numbers_found))
        part_number_returned = subject.part_numbers_found[0]
        self.assertEqual(12, part_number_returned.part_number)
        self.assertEqual([[1, 0], [2, 0]], part_number_returned.coordinates)

        fake_grid = [
            ".12*."
        ]

        subject = GridProcessor(fake_grid)

        self.assertEqual(1, len(subject.part_numbers_found))
        part_number_returned = subject.part_numbers_found[0]
        self.assertEqual(12, part_number_returned.part_number)
        self.assertEqual([[1, 0], [2, 0]], part_number_returned.coordinates)

    def test_grid_process_test2(self):
        fake_grid = [
            "12*",
            "34"
        ]

        subject = GridProcessor(fake_grid)

        self.assertEqual(2, len(subject.part_numbers_found))

        first_part_number_returned = subject.part_numbers_found[0]
        self.assertEqual(12, first_part_number_returned.part_number)
        self.assertEqual([[0, 0], [1, 0]], first_part_number_returned.coordinates)

        second_part_number_returned = subject.part_numbers_found[1]
        self.assertEqual(34, second_part_number_returned.part_number)
        self.assertEqual([[0, -1], [1, -1]], second_part_number_returned.coordinates)

        fake_grid = [
            "12*",
            "34."
        ]

        subject = GridProcessor(fake_grid)

        self.assertEqual(2, len(subject.part_numbers_found))

        first_part_number_returned = subject.part_numbers_found[0]
        self.assertEqual(12, first_part_number_returned.part_number)
        self.assertEqual([[0, 0], [1, 0]], first_part_number_returned.coordinates)

        second_part_number_returned = subject.part_numbers_found[1]
        self.assertEqual(34, second_part_number_returned.part_number)
        self.assertEqual([[0, -1], [1, -1]], second_part_number_returned.coordinates)

        fake_grid = [
            ".12",
            "*34"
        ]

        subject = GridProcessor(fake_grid)

        self.assertEqual(2, len(subject.part_numbers_found))

        first_part_number_returned = subject.part_numbers_found[0]
        self.assertEqual(12, first_part_number_returned.part_number)
        self.assertEqual([[1, 0], [2, 0]], first_part_number_returned.coordinates)

        second_part_number_returned = subject.part_numbers_found[1]
        self.assertEqual(34, second_part_number_returned.part_number)
        self.assertEqual([[1, -1], [2, -1]], second_part_number_returned.coordinates)

        fake_grid = [
            ".12*",
            ".34."
        ]

        subject = GridProcessor(fake_grid)

        self.assertEqual(2, len(subject.part_numbers_found))

        first_part_number_returned = subject.part_numbers_found[0]
        self.assertEqual(12, first_part_number_returned.part_number)
        self.assertEqual([[1, 0], [2, 0]], first_part_number_returned.coordinates)

        second_part_number_returned = subject.part_numbers_found[1]
        self.assertEqual(34, second_part_number_returned.part_number)
        self.assertEqual([[1, -1], [2, -1]], second_part_number_returned.coordinates)

    def test_grid_process_test3(self):
        fake_grid = [
            ".12*34."
        ]

        subject = GridProcessor(fake_grid)

        self.assertEqual(2, len(subject.part_numbers_found))

        first_part_number_returned = subject.part_numbers_found[0]
        self.assertEqual(12, first_part_number_returned.part_number)
        self.assertEqual([[1, 0], [2, 0]], first_part_number_returned.coordinates)

        second_part_number_returned = subject.part_numbers_found[1]
        self.assertEqual(34, second_part_number_returned.part_number)
        self.assertEqual([[4, 0], [5, 0]], second_part_number_returned.coordinates)

    def test_symbol_processing(self):
        fake_grid = [
            "*"
        ]

        subject = GridProcessor(fake_grid)

        self.assertEqual(1, len(subject.symbols_found))
        grid_symbol_returned = subject.symbols_found[0]
        self.assertEqual("*", grid_symbol_returned.symbol)
        self.assertEqual([0, 0], grid_symbol_returned.coordinate)

        fake_grid = [
            ".12.",
            ".34*"
        ]

        subject = GridProcessor(fake_grid)

        self.assertEqual(1, len(subject.symbols_found))
        grid_symbol_returned = subject.symbols_found[0]
        self.assertEqual("*", grid_symbol_returned.symbol)
        self.assertEqual([3, -1], grid_symbol_returned.coordinate)

    def test_symbol_collision(self):
        subject = GridProcessor([
            "....",
            ".12.",
            "...."
        ])
        self.assertEqual(0, len(subject.part_numbers_found))

        def assert_twelve_is_found(subject: GridProcessor):
            self.assertEqual(1, len(subject.part_numbers_found))

            first_part_number_returned = subject.part_numbers_found[0]
            self.assertEqual(12, first_part_number_returned.part_number)
            self.assertEqual([[1, -1], [2, -1]], first_part_number_returned.coordinates)

        subject = GridProcessor([
            "*...",
            ".12.",
            "...."
        ])
        assert_twelve_is_found(subject)

        subject = GridProcessor([
            ".*..",
            ".12.",
            "...."
        ])
        assert_twelve_is_found(subject)

        subject = GridProcessor([
            "..*.",
            ".12.",
            "...."
        ])
        assert_twelve_is_found(subject)

        subject = GridProcessor([
            "...*",
            ".12.",
            "...."
        ])
        assert_twelve_is_found(subject)

        subject = GridProcessor([
            "....",
            "*12.",
            "...."
        ])
        assert_twelve_is_found(subject)

        subject = GridProcessor([
            "....",
            ".12*",
            "...."
        ])
        assert_twelve_is_found(subject)

        subject = GridProcessor([
            "....",
            ".12.",
            "*..."
        ])
        assert_twelve_is_found(subject)

        subject = GridProcessor([
            "....",
            ".12.",
            ".*.."
        ])
        assert_twelve_is_found(subject)

        subject = GridProcessor([
            "....",
            ".12.",
            "..*."
        ])
        assert_twelve_is_found(subject)

        subject = GridProcessor([
            "....",
            ".12.",
            "...*"
        ])
        assert_twelve_is_found(subject)

        subject = GridProcessor([
            "....",
            ".12.",
            "...="
        ])
        assert_twelve_is_found(subject)

        subject = GridProcessor([
            "....",
            ".12.",
            ".../"
        ])
        assert_twelve_is_found(subject)

        subject = GridProcessor([
            "....",
            ".12.",
            "...$"
        ])
        assert_twelve_is_found(subject)

    def test_sum_of_part_numbers_part1(self):
        grid_part_number1 = GridPartNumber()
        grid_part_number1.expand_part_number(12, [])

        grid_part_number2 = GridPartNumber()
        grid_part_number2.expand_part_number(34, [])

        self.assertEqual(46, GridProcessor.calculate_the_sum_of_part_numbers([
            grid_part_number1,
            grid_part_number2
        ]))

        subject = GridProcessor([
            "....",
            ".12.",
            "...$",
            ".34."
        ])
        self.assertEqual(46, subject.sum_of_part_numbers)

    def test_sum_of_part_numbers_part2(self):
        subject = GridProcessor([
            "467..114..",
            "...*......",
            "..35..633.",
            "......#...",
            "617*......",
            ".....+.58.",
            "..592.....",
            "......755.",
            "...$.*....",
            ".664.598.."
        ])

        self.assertEqual(4361, subject.sum_of_part_numbers)


    def test_sum_of_part_numbers_part3(self):
        subject = GridProcessor([
            ".586............*........279..............426..",
            ".*.../.147...744.324.................490.......",
            "1...35....*..........................*...+.....",
            "........411...........................38.26....",
            "../..............789....49.....289.............",
            ".469...798./944...........*....*......237......",
            "........+...........367..274..179.../....*.....",
            "...............498*.............../..657.196...",
            "..+..667...........194.....201...670...........",
            ".90..*.....................*...................",
            "......959.&.............504..........@..-......",
            "...........26......519.......*.....994.855.....",
            "..991.............@...........764..............",
            "....*........782........892.......188&.........",
            "...721..........#.......*...............-......",
            "45.........73........388.............689...11.."
        ])

        self.assertEqual(18486, subject.sum_of_part_numbers)

        # 2 numbers that shouldn't be there:
        # 426 -
        # 73 -