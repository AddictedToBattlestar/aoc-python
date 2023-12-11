from unittest import TestCase
from day8_haunted_wasteland.network_mapper import NetworkMapper
from day8_haunted_wasteland.left_right_step_calculator import calculate, calculate_from_file


class TestLeftRightStepCalculator(TestCase):

    def test_calculate_steps(self):
        network_mapper = NetworkMapper()
        network_mapper.add_nodes([
            "AAA = (BBB, CCC)",
            "BBB = (DDD, AAA)"
        ])
        number_of_steps = calculate(network=network_mapper.network,
                                    instructions="LR",
                                    starting_location="AAA",
                                    target_location="BBB")
        self.assertEqual(1, number_of_steps)

    def test_calculate_steps_example1(self):
        network_mapper = NetworkMapper()
        network_mapper.add_nodes([
            "AAA = (BBB, BBB)",
            "BBB = (AAA, ZZZ)",
            "ZZZ = (ZZZ, ZZZ)"
        ])
        number_of_steps = calculate(network=network_mapper.network,
                                    instructions="LLR",
                                    starting_location="AAA",
                                    target_location="ZZZ")
        self.assertEqual(6, number_of_steps)

    def test_calculate_steps_example2(self):
        network_mapper = NetworkMapper()
        network_mapper.add_nodes([
            "AAA = (BBB, CCC)",
            "BBB = (DDD, EEE)",
            "CCC = (ZZZ, GGG)",
            "DDD = (DDD, DDD)",
            "EEE = (EEE, EEE)",
            "GGG = (GGG, GGG)",
            "ZZZ = (ZZZ, ZZZ)"
        ])
        number_of_steps = calculate(network=network_mapper.network,
                                    instructions="RL",
                                    starting_location="AAA",
                                    target_location="ZZZ")
        self.assertEqual(2, number_of_steps)

    def test_calculate_from_file(self):
        number_of_steps = calculate_from_file(file_name="../day8_haunted_wasteland/day8_data_sample.txt",
                                              starting_location="AAA",
                                              target_location="ZZZ")
        self.assertEqual(6, number_of_steps)