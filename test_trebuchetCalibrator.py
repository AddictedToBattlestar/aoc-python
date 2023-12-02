from unittest import TestCase
from trebuchetCalibrator import get_value

class TestTrebuchetCalibrator(TestCase):
    def test_get_value(self):
        self.assertEquals(get_value("1abc2"), 12)
