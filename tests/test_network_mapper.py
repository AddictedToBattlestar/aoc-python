from unittest import TestCase
from day8_haunted_wasteland.network_mapper import NetworkMapper


class TestNetworkMapper(TestCase):
    def test_add_node(self):
        subject = NetworkMapper()
        subject.add_node("AAA = (BBB, CCC)")
        self.assertEqual({"AAA": ("BBB", "CCC")}, subject.network)

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