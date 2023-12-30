from __future__ import annotations

from functools import total_ordering
from enum import IntEnum
from collections import Counter

class Rank(IntEnum):
    HIGH = 0
    PAIR = 1
    PAIRS = 2
    THREE = 3
    FULL = 4
    FOUR = 5
    FIVE = 6

# strengh order is A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2
cardmap = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
}

@total_ordering
class Hand():
    hand: list[int]
    bid: int
    rank: Rank

    def __init__(self, bid:int, hand: list[int]):
        self.bid = bid
        self.hand = hand
        if 11 in self.hand:
            self.replace_jokers()
        else:
            self.compute_rank()

    @classmethod
    def parse(cls, line:str) -> Hand:
        splitted = line.split()
        return Hand(int(splitted[1]), list(cardmap[c] for c in splitted[0]))

    def replace_jokers(self):
        others = set(self.hand)
        others.remove(11)
        if others:
            possible = [
                Hand(0, [o if c==11 else c for c in self.hand])
                for o in others
            ]
            possible.sort()
            best = possible.pop()
            self.rank = best.rank
        else:
            self.rank = Rank.FIVE

    def compute_rank(self):
        distinct = Counter(self.hand)
        if len(distinct) == 5:
            self.rank = Rank.HIGH
        elif len(distinct) == 4:
            self.rank = Rank.PAIR
        elif len(distinct) == 3:
            for k in distinct.values():
                if k == 3:
                    self.rank = Rank.THREE
                    break
            else:
                self.rank = Rank.PAIRS
        elif len(distinct) == 2:
            for k in distinct.values():
                if k == 4:
                    self.rank = Rank.FOUR
                    break
            else:
                self.rank = Rank.FULL
        elif len(distinct) == 1:
            self.rank = Rank.FIVE
        else:
            raise ValueError()

    def __eq__(self, __value: object) -> bool:
        return (isinstance(__value, Hand) and
                self.hand == __value.hand
                )

    def __lt__(self, __value: object) -> bool:
        if not isinstance(__value, Hand):
            return False
        if self.rank < __value.rank:
            return True
        elif self.rank > __value.rank:
            return False
        else:
            for i in range(5):
                if self.hand[i] < __value.hand[i]:
                    return True
                elif self.hand[i] > __value.hand[i]:
                    return False

    def __repr__(self) -> str:
        return f"Hand({self.hand}, {self.rank}, {self.bid})"

def today(data:list[str]) -> int:
    total = 0
    hands = [Hand.parse(line) for line in data]
    hands.sort()
    for i, h in enumerate(hands):
        rank = i + 1
        total += rank * h.bid
    return total
