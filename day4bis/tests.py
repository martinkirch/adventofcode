from unittest import TestCase
from . import today, Card, load_cards

test_data = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
""".strip().split('\n')

class TodayTest(TestCase):
    def test_load_cards(self):
        cards = load_cards(test_data)
        self.assertEqual(len(cards), 6)

    def test_card(self):
        c = Card.from_line("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53")
        self.assertEqual(c.points, 4)
        self.assertEqual(c.instances, 1)
        c = Card.from_line("Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36")
        self.assertEqual(c.points, 0)

    def test_data(self):
        self.assertEqual(today(test_data), 30)
