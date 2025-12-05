from __future__ import annotations

class Card:
    def __init__(self, winning:set[int], having:set[int]):
        self.winning = winning
        self.having = having
        self.instances = 1
    
    @classmethod
    def from_line(cls, line:str) -> Card:
        id_numbers = line.split(':')
        numbers = id_numbers[1].split('|')

        winning = set(int(n) for n in numbers[0].split())
        having = set(int(n) for n in numbers[1].split())

        return cls(winning, having)

    @property
    def points(self):
        return len(self.winning.intersection(self.having))

def load_cards(data:list[str]) -> list[Card]:
    cards = []
    for line in data:
        if line:
            cards.append(Card.from_line(line))
    return cards

def today(data:list[str]) -> int:
    total = 0
    cards = load_cards(data)
    for i, card in enumerate(cards):
        total += card.instances
        for j in range(i+1, i+1+card.points):
            cards[j].instances += card.instances
    return total
