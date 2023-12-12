from unittest import TestCase
from . import today, line_value, lettersdigit

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
    
    def test_re(self):
        self.assertEqual(lettersdigit.sub(lambda x: "<"+x.group(0)+">", "zoneight234"), "z<one>ight234")
        self.assertEqual(lettersdigit.sub(lambda x: "<"+x.group(0)+">", "pqr3stu8vwx"), "pqr3stu8vwx")
        self.assertEqual(lettersdigit.sub(lambda x: "<"+x.group(0)+">", "eightwothree"), "<eight>wo<three>")
        self.assertEqual(lettersdigit.sub(lambda x: "<"+x.group(0)+">", "onone"), "on<one>")
        
