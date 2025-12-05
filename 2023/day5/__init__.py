from dataclasses import dataclass

@dataclass
class Range():
    start:int
    end:int
    delta:int

    def __init__(self, line:str):
        splitted = line.split()
        if not splitted:
            print(repr(line))
        self.start = int(splitted[1])
        self.end = self.start + int(splitted[2])
        self.delta = int(splitted[0]) - self.start

def do(locations:list[int], mapping:list[Range]) -> list[int]:
    mapped = []
    for l in locations:
        for map in mapping:
            if map.start <= l and l < map.end:
                mapped.append(l + map.delta)
                break
        else:
            mapped.append(l)
    return mapped

def today(data:list[str]) -> int:
    lines = iter(data)
    locations = [int(i) for i in next(lines)[7:].split()]
    mapping = []
    try:
        while True:
            line = next(lines).strip()
            if not line:
                if mapping:
                    locations = do(locations, mapping)
                    mapping = []
            elif "map" in line:
                pass
            else:
                mapping.append(Range(line))

    except StopIteration:
        locations = do(locations, mapping)
    return min(locations)
