from enum import Enum
from itertools import count
lines = open("day14_input.txt").readlines()

# it's simpler to note map[x][y] so our axes are inverted - source will be at 0,500

max_x = 0
max_y = 0
for line in lines:
    for point in line.split(' -> '):
        splitted = point.split(',')
        x = int(splitted[1])
        y = int(splitted[0])
        max_x = max(max_x, x)
        max_y = max(max_y, y)
max_x += 1
max_y += 1

print(f"size is {max_x},{max_y}")

class Matter(Enum):
    AIR = 0
    ROCK = 1
    SAND = 2

def val_to_str(item):
    match item:
        case Matter.AIR:
            return '.'
        case Matter.ROCK:
            return '#'
        case Matter.SAND:
            return 'o'
        case _:
            return '' 

def build_map():
    map = [
        [Matter.AIR]*max_y for x in range(max_x)
    ]

    def draw_line(start, dest):
        nonlocal map
        if start[0] == dest[0]:
            y1 = min(start[1], dest[1])
            y2 = max(start[1], dest[1]) + 1
            for y in range(y1, y2):
                map[start[0]][y] = Matter.ROCK
        elif start[1] == dest[1]:
            x1 = min(start[0], dest[0])
            x2 = max(start[0], dest[0]) + 1
            for x in range(x1, x2):
                map[x][start[1]] = Matter.ROCK
        else:
            raise ValueError("mmmh")

    for line in lines:
        previous = None
        current = None
        for point in line.split(' -> '):
            splitted = point.split(',')
            current = (int(splitted[1]), int(splitted[0]))
            if previous:
                draw_line(previous, current)
            previous = current
    return map

map = build_map()

def print_map():
    for l in map:
        print(''.join([val_to_str(x) for x in l]))

def pour():
    # "sand is pouring into the cave from point 500,0."
    x = 0
    y = 500
    max_x = len(map) - 1
    max_y = len(map[0]) - 1
    while map[x][y] == Matter.AIR:
        # down one step
        if x == max_x:
            raise ValueError("falling down")
        elif map[x+1][y] == Matter.AIR:
            x += 1
            continue
        
        # one step down, and to the left
        if y > 0:
            if map[x+1][y-1] == Matter.AIR:
                x += 1
                y -= 1
                continue
        else:
            print("phase2 error")
        
        # one step down and to the right
        if y < max_y:
            if map[x+1][y+1] == Matter.AIR:
                x += 1
                y += 1
                continue
        else:
            print("phase2 error2")
        
        # rest !
        map[x][y] = Matter.SAND
        return
    raise RuntimeError("This should not happen")

for nb in count():
    try:
        pour()
    except ValueError:
        break

print(f"phase1: {nb} units of sand come to rest before sand starts flowing into the abyss below")

#phase 2:
max_y += max_x
map = build_map()
map.append([Matter.AIR]*max_y)
map.append([Matter.ROCK]*max_y)

for nb in count():
    try:
        pour()
    except RuntimeError:
        break

# print_map()
print(f"phase2: {nb} units of sand come to rest before sand reaches source")
