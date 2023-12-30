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

# strengh order is A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, or 2
cardmap = {
    'A': 13,
    'K': 12,
    'Q': 11,
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

    def __init__(self, line:str):
        splitted = line.split()
        self.hand = list(cardmap[c] for c in splitted[0])
        self.bid = int(splitted[1])

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
    hands = [Hand(line) for line in data]
    hands.sort()
    for i, h in enumerate(hands):
        rank = i + 1
        total += rank * h.bid
    return total
