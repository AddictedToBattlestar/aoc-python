from unittest import TestCase
from day8_haunted_wasteland.left_right_step_calculator import LeftRightStepCalculator


class TestLeftRightStepCalculator(TestCase):
    def test_add_node(self):
        subject = LeftRightStepCalculator()
        subject.add_node("AAA = (BBB, CCC)")
        self.assertEqual({"AAA": ("BBB", "CCC")}, subject.network)

    def test_add_nodes(self):
        subject = LeftRightStepCalculator()
        subject.add_nodes([
            "AAA = (BBB, BBB)",
            "BBB = (AAA, AAA)"
        ])
        self.assertEqual({
            "AAA": ("BBB", "BBB"),
            "BBB": ("AAA", "AAA")
        }, subject.network)

    def test_calculate_steps(self):
        subject = LeftRightStepCalculator()
        subject.add_nodes([
            "AAA = (BBB, CCC)",
            "BBB = (DDD, AAA)"
        ])
        number_of_steps = subject.calculate("LR", "AAA", "BBB")
        self.assertEqual(1, number_of_steps)

    def test_calculate_steps_example1(self):
        subject = LeftRightStepCalculator()
        subject.add_nodes([
            "AAA = (BBB, BBB)",
            "BBB = (AAA, ZZZ)",
            "ZZZ = (ZZZ, ZZZ)"
        ])
        number_of_steps = subject.calculate("LLR", "AAA", "ZZZ")
        self.assertEqual(6, number_of_steps)

    def test_calculate_steps_example2(self):
        subject = LeftRightStepCalculator()
        subject.add_nodes([
            "AAA = (BBB, CCC)",
            "BBB = (DDD, EEE)",
            "CCC = (ZZZ, GGG)",
            "DDD = (DDD, DDD)",
            "EEE = (EEE, EEE)",
            "GGG = (GGG, GGG)",
            "ZZZ = (ZZZ, ZZZ)"
        ])
        number_of_steps = subject.calculate("RL", "AAA", "ZZZ")
        self.assertEqual(2, number_of_steps)

    def test_calculate_from_file(self):
        subject = LeftRightStepCalculator()
        number_of_steps = subject.calculate_from_file(file_name="../day8_haunted_wasteland/day8_data_sample.txt",
                                                      starting_location="AAA",
                                                      target_location="ZZZ")
        self.assertEqual(6, number_of_steps)
