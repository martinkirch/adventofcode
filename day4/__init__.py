from __future__ import annotations

class Card:
    def __init__(self, winning:set[int], having:set[int]):
        self.winning = winning
        self.having = having
    
    @classmethod
    def from_line(cls, line:str) -> Card:
        id_numbers = line.split(':')
        numbers = id_numbers[1].split('|')

        winning = set(int(n) for n in numbers[0].split())
        having = set(int(n) for n in numbers[1].split())

        return cls(winning, having)

    @property
    def points(self):
        matching = len(self.winning.intersection(self.having))
        if matching == 0:
            return 0
        else:
            return 2 ** (matching - 1)

def today(data:list[str]) -> int:
    total = 0
    for line in data:
        if line:
            card = Card.from_line(line)
            total += card.points
    return total
