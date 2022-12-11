lines = open("day10_input.txt").readlines()

x = 1
cycle = 0
strength = 0
screen = []
for i in range(6):
    screen.append(['.'] * 40)

def update_strength():
    global strength, cycle, x
    if (cycle % 40) == 20:
        strength += cycle * x

def draw():
    global cycle, x, screen
    row = cycle // 40
    pixel_pos = cycle % 40
    if x == pixel_pos or (x-1) == pixel_pos or (x+1) == pixel_pos:
        screen[row][pixel_pos] = '#'

for line in lines:
    if line.startswith("noop"):
        draw()
        cycle += 1
        update_strength()
    else:
        draw()
        val = int(line.split()[1])
        cycle += 1
        update_strength()
        draw()
        cycle += 1
        update_strength()
        x += val

print(strength)

for l in screen:
    print(''.join(l))
    
