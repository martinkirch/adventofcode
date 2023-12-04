from unittest import TestCase
from . import today

test_data = """
"""

class TodayTest(TestCase):
    def test_data(self):
        self.assertEqual(today(test_data), 0)
