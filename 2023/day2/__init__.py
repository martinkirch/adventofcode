#!/usr/bin/env python3
from __future__ import annotations
from dataclasses import dataclass, field

@dataclass
class Picked():
    blue: int = 0
    red: int = 0
    green: int = 0

    @staticmethod
    def from_entry(input:str) -> Picked:
        picked = Picked()
        for number in input.split(','):
            couple = number.split()
            setattr(picked, couple[1], int(couple[0]))
        return picked

    def possible(self, blue:int, red:int, green:int) -> bool:
        return (
            self.blue <= blue and
            self.red <= red and
            self.green <= green
        )

@dataclass
class Game():
    id: int
    picks: list[Picked] = field(default_factory=list)

    @staticmethod
    def from_line(input:str) -> Game:
        split = input.split(":")
        game = Game(id=int(split[0][5:]))
        for pick in split[1].split(';'):
            game.picks.append(Picked.from_entry(pick))
        return game

    def possible(self, blue:int, red:int, green:int) -> bool:
        for pick in self.picks:
            if not pick.possible(blue, red, green):
                return False
        return True

    def power(self) -> int:
        maxpick = Picked()
        for pick in self.picks:
            if pick.blue > maxpick.blue:
                maxpick.blue = pick.blue
            if pick.red > maxpick.red:
                maxpick.red = pick.red
            if pick.green > maxpick.green:
                maxpick.green = pick.green
        return maxpick.red * maxpick.green * maxpick.blue


def today_1(data:str) -> int:
    total = 0
    for line in data.split('\n'):
        line = line.strip()
        if not line:
            continue
        game = Game.from_line(line)
        if game.possible(14, 12, 13):
            total += game.id
    return total

def today(data:str) -> int:
    total = 0
    for line in data.split('\n'):
        line = line.strip()
        if not line:
            continue
        game = Game.from_line(line)
        total += game.power()
    return total
