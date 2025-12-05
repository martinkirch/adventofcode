from itertools import cycle

instructions_map = {
    'L': 0,
    'R': 1,
}

def today(data:list[str]) -> int:
    instructions = [instructions_map[c] for c in data[0].strip()]

    network = {}
    for l in data[2:]:
        network[l[0:3]] = (l[7:10], l[12:15])
    
    steps = 0
    current = 'AAA'
    reader = iter(cycle(instructions))
    while current != 'ZZZ':
        steps += 1
        current = network[current][next(reader)]
    return steps
