from unittest import TestCase
from . import today, Hand, Rank

test_data = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
""".strip().split('\n')

class TodayTest(TestCase):
    def test_hand(self):
        h = Hand.parse('32T3K 765')
        self.assertEqual(h.bid, 765)
        self.assertListEqual(h.hand, [3, 2, 10, 3, 13])

        self.assertEqual(Hand.parse('32T3K 765').rank, Rank.PAIR)
        self.assertEqual(Hand.parse('KK677 765').rank, Rank.PAIRS)
        self.assertEqual(Hand.parse('Q2QJA 765').rank, Rank.THREE)
        self.assertEqual(Hand.parse('32T6K 765').rank, Rank.HIGH)
        self.assertEqual(Hand.parse('32332 765').rank, Rank.FULL)
        self.assertEqual(Hand.parse('32333 765').rank, Rank.FOUR)
        self.assertEqual(Hand.parse('22222 765').rank, Rank.FIVE)
        
        self.assertEqual(Hand.parse('QJ725 765').rank, Rank.PAIR)
        self.assertEqual(Hand.parse('QQQJA 765').rank, Rank.FOUR)
        self.assertEqual(Hand.parse('T55J5 765').rank, Rank.FOUR)
        self.assertEqual(Hand.parse('KTJJT 765').rank, Rank.FOUR)
 
    def test_ordering(self):
        self.assertLess(Hand.parse("32T3K 765"), Hand.parse("KK677 28"))
        self.assertLess(Hand.parse("KK677 28"), Hand.parse("T55J5 684"))
        self.assertLess(Hand.parse("T55J5 684"), Hand.parse("QQQJA 483"))
        self.assertLess(Hand.parse("QQQJA 483"), Hand.parse("KTJJT 220"))

        self.assertLess(Hand.parse("JJJJJ 220"), Hand.parse("22222 483"))

        self.assertEqual(Hand.parse("QJJQ2 0").rank, Hand.parse("QQQQ2 0").rank)
        self.assertLess(Hand.parse("QJJQ2 0"), Hand.parse("QQQQ2 0"))

        self.assertEqual(Hand.parse("JKKK2 0").rank, Hand.parse("QQQQ2 0").rank)
        self.assertLess(Hand.parse("JKKK2 0"), Hand.parse("QQQQ2 0"))

        self.assertEqual(Hand.parse("JKJKK 0").rank, Hand.parse("KKKKK 0").rank)
        self.assertLess(Hand.parse("JKJKK 0"), Hand.parse("KKKKK 0"))

        self.assertEqual(Hand.parse("JKKKK 0").rank, Hand.parse("KKKKK 0").rank)
        self.assertLess(Hand.parse("JKKKK 0"), Hand.parse("KKKKK 0"))


    def test_data(self):
        self.assertEqual(today(test_data), 5905)
