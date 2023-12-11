from unittest import TestCase

from day8_haunted_wasteland.network_mapper import NetworkMapper
from day8_haunted_wasteland.revised_left_right_step_calculator import calculate, calculate_from_file


class Test(TestCase):
    def test_calculate_steps_example1(self):
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
        number_of_steps = calculate(starting_location_ids=network_mapper.starting_node_ids,
                                    network=network_mapper.network,
                                    instructions="LR")
        self.assertEqual(6, number_of_steps)

    def test_calculate_from_file(self):
        number_of_steps = calculate_from_file(file_name="../day8_haunted_wasteland/day8_data_sample.txt")
        self.assertEqual(6, number_of_steps)