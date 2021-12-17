smol_input = """11111
19991
19191
19991
11111"""

test_input = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""

challenge_input = """2478668324
4283474125
1663463374
1738271323
4285744861
3551311515
8574335438
7843525826
1366237577
3554687226"""

INPUT = challenge_input

map = [[int(c) for c in line] for line in INPUT.split()]
width = len(map)
jmax = width - 1
nb_octopuses = width * width

def step_start():
    contain_10 = False
    for i in range(width):
        for j in range(width):
            map[i][j] += 1
            contain_10 = contain_10 or map[i][j] == 10
    return contain_10

def flash_maybe(i, j):
    if map[i][j] in (0, 10):
        return False #flashed already, or is waiting to flash
    else:
        map[i][j] += 1
        return map[i][j] == 10

def spread(i, j):
    flash_found = False
    if i > 0:
        flash_found = flash_maybe(i-1, j) or flash_found
        if j > 0:
            flash_found = flash_maybe(i-1, j-1) or flash_found
        if j < jmax:
            flash_found = flash_maybe(i-1, j+1) or flash_found
    if i < jmax:
        flash_found = flash_maybe(i+1, j) or flash_found
        if j > 0:
            flash_found = flash_maybe(i+1, j-1) or flash_found
        if j < jmax:
            flash_found = flash_maybe(i+1, j+1) or flash_found
    if j > 0:
        flash_found = flash_maybe(i, j-1) or flash_found
    if j < jmax:
        flash_found = flash_maybe(i, j+1) or flash_found
    return flash_found


def flash():
    found = 0
    flashes_remaining = False
    for i in range(width):
        for j in range(width):
            if map[i][j] == 10:
                found += 1
                flashes_remaining = spread(i, j) or flashes_remaining
                map[i][j] = 0
    return (flashes_remaining, found)

def step():
    flashes = 0
    flashes_remaining = step_start()
    while flashes_remaining:
        (flashes_remaining, found) = flash()
        flashes += found
    return flashes

total = 0
for i in range(1000):
    step_flashes = step()
    if step_flashes == nb_octopuses:
        print(f"All flashing at step {i+1}")
        break
    total += step_flashes

for line in map:
    print(line)

print(f"\ntotal {total} flashes")
