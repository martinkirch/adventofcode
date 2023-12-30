from unittest import TestCase
from . import today

test_data = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
""".strip().split('\n')

class TodayTest(TestCase):
    def test_data(self):
        self.assertEqual(today(test_data), 6)
