from __future__ import annotations
from typing import Generator
from functools import total_ordering
from heapq import *
lines = open("day12_input.txt").readlines()

raw_map = []
start = None
dest = None
for x, line in enumerate(lines):
    y_S = line.find('S')
    if y_S >=0:
        start = (x, y_S)
        line = line.replace('S', 'a')
    y_E = line.find('E')
    if y_E >=0:
        dest = (x, y_E)
        line = line.replace('E', 'z')
    raw_map.append([ord(c) for c in line])

@total_ordering
class Point:
    def __init__(self, x, y, height) -> Point:
        self.x = x
        self.y = y
        self.height = height
        self.dist_from_start = None
        self.min_to_dest = 99999999999
        self.bird_dist_to_end = abs(x - dest[0]) + abs(y - dest[1])
    
    def update_dist_from_start(self, dist):
        if not self.dist_from_start or dist < self.dist_from_start - 1:
            self.dist_from_start = dist + 1
            self.min_to_dest = self.dist_from_start + self.bird_dist_to_end
            return True
        return False

    def __eq__(self, __o: object) -> bool:
        return (isinstance(__o, Point)
            and __o.min_to_dest == self.min_to_dest
        )

    def __lt__(self, __o: object) -> bool:
        """
        sort by [current known distance from start] + [bird dist to end]
        """
        return (isinstance(__o, Point)
            and self.min_to_dest < __o.min_to_dest
        )
    
height = len(raw_map) - 1
width = len(raw_map[0]) - 1

class Finder:
    def __init__(self, s_x, s_y):
        self.map = [
            [Point(x, y, h) for (y, h) in enumerate(row)]
            for (x, row) in enumerate(raw_map)
        ]
        self.map[s_x][s_y].dist_from_start = 0
        self.candidates:list[Point] = []
        heappush(self.candidates, self.map[s_x][s_y])

    def gen_neighbour(self, current:Point) -> Generator[Point]:
        if current.y > 0:
            yield self.map[current.x][current.y-1]
        if current.y < width:
            yield self.map[current.x][current.y+1]
        if current.x > 0:
                yield self.map[current.x-1][current.y]
        if current.x < height:
                yield self.map[current.x+1][current.y]

    def shortest(self) -> int:
        while(self.candidates):
            current = heappop(self.candidates)
            for neighbour in self.gen_neighbour(current):
                if neighbour.height <= current.height + 1:
                    if neighbour.update_dist_from_start(current.dist_from_start):
                        heappush(self.candidates, neighbour)

        return self.map[dest[0]][dest[1]].dist_from_start

print(f"Phase1: {Finder(start[0], start[1]).shortest()}")

lengths = []
for x, row in enumerate(raw_map):
    for y, h in enumerate(row):
        if h == ord('a'):
            length = Finder(x, y).shortest()
            if length:
                lengths.append(length)
lengths.sort()
print(lengths[0])
