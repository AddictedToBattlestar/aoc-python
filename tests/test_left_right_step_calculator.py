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
                                    starting_location_id="AAA",
                                    target_location_id="BBB")
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
                                    starting_location_id="AAA",
                                    target_location_id="ZZZ")
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
                                    starting_location_id="AAA",
                                    target_location_id="ZZZ")
        self.assertEqual(2, number_of_steps)

    def test_calculate_from_file(self):
        number_of_steps = calculate_from_file(file_name="../day8_haunted_wasteland/day8_data_sample.txt",
                                              starting_location_id="AAA",
                                              target_location_id="ZZZ")
        self.assertEqual(6, number_of_steps)

    def test_calculate_steps_to_partial_example1(self):
        network_mapper = NetworkMapper()
        network_mapper.add_nodes([
            "11A = (11B, XXX)",
            "11B = (XXX, 11Z)",
            "11Z = (11B, XXX)",
            "22A = (22B, XXX)",
            "22B = (22C, 22C)",
            "22C = (22Z, 22Z)",
            "22Z = (22B, 22B)",
            "XXX = (XXX, XXX)"
        ])
        number_of_steps, location_id_reached = calculate(network=network_mapper.network,
                                                         instructions="LR",
                                                         starting_location_id="11A")
        self.assertEqual(2, number_of_steps)
        self.assertEqual("11Z", location_id_reached)

        number_of_steps, location_id_reached = calculate(network=network_mapper.network,
                                                         instructions="LR",
                                                         starting_location_id="22A")
        self.assertEqual(3, number_of_steps)
        self.assertEqual("22Z", location_id_reached)
