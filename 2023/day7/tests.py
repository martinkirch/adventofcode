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
        h = Hand('32T3K 765')
        self.assertEqual(h.bid, 765)
        self.assertListEqual(h.hand, [3, 2, 10, 3, 13])

        self.assertEqual(Hand('32T3K 765').rank, Rank.PAIR)
        self.assertEqual(Hand('T55J5 765').rank, Rank.THREE)
        self.assertEqual(Hand('KK677 765').rank, Rank.PAIRS)
        self.assertEqual(Hand('KTJJT 765').rank, Rank.PAIRS)
        self.assertEqual(Hand('QQQJA 765').rank, Rank.THREE)
        self.assertEqual(Hand('32T6K 765').rank, Rank.HIGH)
        self.assertEqual(Hand('32332 765').rank, Rank.FULL)
        self.assertEqual(Hand('32333 765').rank, Rank.FOUR)
        self.assertEqual(Hand('22222 765').rank, Rank.FIVE)
 
    def test_ordering(self):
        self.assertLess(Hand("32T3K 765"), Hand("KTJJT 220"))
        self.assertLess(Hand("KTJJT 220"), Hand("KK677 28"))
        self.assertLess(Hand("KK677 28"), Hand("T55J5 684"))
        self.assertLess(Hand("T55J5 684"), Hand("QQQJA 483"))

    def test_data(self):
        self.assertEqual(today(test_data), 6440)
