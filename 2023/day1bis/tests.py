from unittest import TestCase
from . import today, line_value

test_data = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
""".strip().split('\n')

class TodayTest(TestCase):
    def test_data(self):
        self.assertEqual(today(test_data), 281)
    
    def test_line(self):
        self.assertEqual(line_value('zoneight234'), 14)
        self.assertEqual(line_value('pqr3stu8vwx'), 38)
        self.assertEqual(line_value('eightwothree'), 83)
        self.assertEqual(line_value('1oneight'), 18)
        
