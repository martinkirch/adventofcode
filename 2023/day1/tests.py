from unittest import TestCase
from . import today, line_value

test_data = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
""".strip().split('\n')

class TodayTest(TestCase):
    def test_data(self):
        self.assertEqual(today(test_data), 142)
    
    def test_line(self):
        self.assertEqual(line_value('1abc2'), 12)
        self.assertEqual(line_value('pqr3stu8vwx'), 38)
        self.assertEqual(line_value('a1b2c3d4e5f'), 15)
        self.assertEqual(line_value('treb7uchet'), 77)
