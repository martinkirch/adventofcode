#!/usr/bin/env python3

from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Number():
    n: int
    seen: bool = False

def parse_line(input_line:str, mode_bis=False) -> list[Number|bool]:
    line = []
    stack = None

    def purge_stack():
        nonlocal stack
        if stack is not None:
            n = Number(n=int(stack))
            for i in range(len(stack)):
                line.append(n)
            stack = None

    for c in input_line:
        if c.isdigit():
            if stack is None:
                stack = c
            else:
                stack += c
        elif c == '.' or (mode_bis and c != '*'):
            purge_stack()
            line.append(False)
        else:
            purge_stack()
            line.append(True)

    purge_stack()
    return line

def unseen_numbers_around(map, x, y) -> int:
    total = 0
    for i in range(x-1, x+2):
        if i < 0:
            continue
        for j in range(y-1, y+2):
            if j < 0:
                continue
            try:
                cell = map[i][j]
            except IndexError:
                continue
            if isinstance(cell, Number) and not cell.seen:
                cell.seen = True
                total += cell.n
    return total

def reset_seen(m):
    for row in m:
        for cell in row:
            if isinstance(cell, Number):
                cell.seen = False

def adjacent_numbers(m, x, y) -> list[int]:
    reset_seen(m)
    adjacent = []
    for i in range(x-1, x+2):
        if i < 0:
            continue
        for j in range(y-1, y+2):
            if j < 0:
                continue
            try:
                cell = m[i][j]
            except IndexError:
                continue
            if isinstance(cell, Number) and not cell.seen:
                cell.seen = True
                adjacent.append(cell.n)
    return adjacent

def today_1(data:str) -> int:
    map = []
    total = 0
    for l in data.split("\n"):
        if l:
            map.append(parse_line(l))
    for (x, row) in enumerate(map):
        for (y, cell) in enumerate(row):
            if cell is True:
                total += unseen_numbers_around(map, x, y)
    return total

def today(data:str) -> int:
    map = []
    total = 0
    for l in data.split("\n"):
        if l:
            map.append(parse_line(l, mode_bis=True))
    for (x, row) in enumerate(map):
        for (y, cell) in enumerate(row):
            if cell is True:
                adjacent = adjacent_numbers(map, x, y)
                if len(adjacent) == 2:
                    total += adjacent[0] * adjacent[1]
    return total
