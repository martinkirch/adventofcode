from unittest import TestCase
from . import today

test_data = """Time:      7  15   30
Distance:  9  40  200
""".strip().split('\n')

class TodayTest(TestCase):
    def test_data(self):
        self.assertEqual(today(test_data), 288)
