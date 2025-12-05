from __future__ import annotations
from dataclasses import dataclass

@dataclass(order=True)
class Range():
    start:int
    end:int
    delta:int

    @classmethod
    def from_line(cls, line:str):
        splitted = line.split()
        if not splitted:
            print(repr(line))
        start = int(splitted[1])
        end = start + int(splitted[2])
        delta = int(splitted[0]) - start
        return Range(start, end, delta)

    def split(self, mapping:list[Range]) -> list[Range]:
        """
        assuming mapping is sorted and filled
        """
        splitted = []
        for m in mapping:
            if m.end <= self.start:
                continue
            elif self.end <= m.start:
                break
            else:
                splitted.append(Range(
                    max(m.start, self.start) + m.delta,
                    min(m.end, self.end) + m.delta,
                    0,
                ))
        return splitted

def do(locations:list[Range], mapping:list[Range]) -> list[Range]:
    mapped = []
    for l in locations:
        mapped.extend(l.split(mapping))
    return mapped

INF = 99999999999

def fill(mapping:list[Range]) -> list[Range]:
    filled = []
    covered = 0
    for m in mapping:
        if m.start > covered:
            filled.append(Range(covered, m.start, 0))
        filled.append(m)
        covered = m.end
    if covered < INF:
        filled.append(Range(covered, INF, 0))
    return filled

def today(data:list[str]) -> int:
    lines = iter(data)
    raw = [int(i) for i in next(lines)[7:].split()]
    locations = []
    for i in range(0, len(raw), 2):
        locations.append(Range(raw[i], raw[i]+raw[i+1], 0))
    mapping = []
    try:
        while True:
            line = next(lines).strip()
            if not line:
                if mapping:
                    mapping.sort()
                    mapping = fill(mapping)
                    locations = do(locations, mapping)
                    mapping = []
            elif "map" in line:
                pass
            else:
                mapping.append(Range.from_line(line))

    except StopIteration:
        mapping.sort()
        mapping = fill(mapping)
        locations = do(locations, mapping)
    return min(locations).start
