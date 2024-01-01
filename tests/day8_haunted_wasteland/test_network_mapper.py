from unittest import TestCase
from src.day8_haunted_wasteland.network_mapper import NetworkMapper


class TestNetworkMapper(TestCase):
    def test_add_node(self):
        subject = NetworkMapper()
        subject.add_node("AAA = (BBB, CCC)")
        self.assertEqual({"AAA": ("BBB", "CCC")}, subject.network)
        self.assertEqual(["AAA"], subject.starting_node_ids)

    def test_add_nodes(self):
        subject = NetworkMapper()
        subject.add_nodes([
            "AAA = (BBB, BBB)",
            "BBB = (AAA, AAA)"
        ])
        self.assertEqual({
            "AAA": ("BBB", "BBB"),
            "BBB": ("AAA", "AAA")
        }, subject.network)
        self.assertEqual(["AAA"], subject.starting_node_ids)

    def test_starting_nodes(self):
        subject = NetworkMapper()
        self.assertEqual([], subject.starting_node_ids)
        subject.add_nodes([
            "AAA = (BBB, BBB)",
            "BBB = (AAA, AAA)",
            "BBA = (BBB, AAA)",
            "ABB = (AAA, BBB)",
            "AAB = (BBB, AAA)"
        ])
        self.assertEqual(["AAA", "BBA"], subject.starting_node_ids)

    def test_terminating_nodes(self):
        subject = NetworkMapper()
        self.assertEqual([], subject.terminating_node_ids)
        subject.add_nodes([
            "AAA = (BBB, BBB)",
            "ZZZ = (AAA, AAA)",
            "ZZA = (BBB, AAA)",
            "AZZ = (AAA, BBB)",
            "AAZ = (BBB, AAA)"
        ])
        self.assertEqual(["ZZZ", "AZZ", "AAZ"], subject.terminating_node_ids)

