from itertools import cycle

instructions_map = {
    'L': 0,
    'R': 1,
}

def all_z(points:list[str]) -> bool:
    for p in points:
        if p[-1] != 'Z':
            return False
    return True

def today(data:list[str]) -> int:
    instructions = [instructions_map[c] for c in data[0].strip()]

    network = {}
    for l in data[2:]:
        network[l[0:3]] = (l[7:10], l[12:15])

    steps = 0
    current = []
    for point in network:
        if point[-1] == 'A':
            current.append(point)
    reader = iter(cycle(instructions))

    while not all_z(current):
        steps += 1
        instruction = next(reader)
        current = [network[c][instruction] for c in current]
    return steps
