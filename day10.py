lines = open("day10_input.txt").readlines()

x = 1
cycle = 0
strength = 0

def update_strength():
    global strength, cycle, x
    if (cycle % 40) == 20:
        strength += cycle * x

for line in lines:
    if line.startswith("noop"):
        cycle += 1
        update_strength()
    else:
        val = int(line.split()[1])
        cycle += 1
        update_strength()
        cycle += 1
        update_strength()
        x += val

print(strength)
        
    
