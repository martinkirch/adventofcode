from itertools import cycle
from math import lcm

instructions_map = {
    'L': 0,
    'R': 1,
}

def find_cycles(s, network, reader):
    steps = 0
    current = s
    seen = set()
    while current not in seen:
        if current[-1] == 'Z':
            seen.add(current)
            steps += 1
            current = network[current][next(reader)]
        while current[-1] != 'Z':
            steps += 1
            current = network[current][next(reader)]

        print(f"start at {s}, arrive at {current} in {steps} steps")
        return steps # comment this, let it run, read the input and note how start/end nodes go to almost the same nodes

    print(f"start at {s}, cycle to {current} in {steps} steps\n")

def lcm_simple(items:list[int]) -> int:
    "Returns the least common multiplier of items"
    current = list(items)
    while True:
        smallest = current[0]
        greatest = current[0]
        smallest_i = 0
        for (i, item) in enumerate(current):
            if item < smallest:
                smallest = item
                smallest_i = i
            if item > greatest:
                greatest = item
        if smallest == greatest:
            return smallest
        else:
            current[smallest_i] = current[smallest_i] + items[smallest_i]

def today(data:list[str]) -> int:
    instructions = [instructions_map[c] for c in data[0].strip()]
    print(f"len(instructions)={len(instructions)}")

    network = {}
    for l in data[2:]:
        network[l[0:3]] = (l[7:10], l[12:15])

    starters = []
    for point in network:
        if point[-1] == 'A':
            starters.append(point)

    gears = [len(instructions)]
    for starter in starters:
        gears.append(find_cycles(starter, network, iter(cycle(instructions))))

    return lcm(*gears)
