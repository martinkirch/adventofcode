from unittest import TestCase
from . import today

test_data = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
""".strip().split('\n')

class TodayTest(TestCase):
    def test_data(self):
        self.assertEqual(today(test_data), 6)
