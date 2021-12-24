"""
Day17 "trick shot"

y0 and x0 are 0

x(t) = x(t_prev) + max(Vx - t + 1, 0) 
y(t) = y(t_prev) + Vy - t + 1

"""
from math import sqrt

test_input = [[20,30],[-10,-5]]
puzzle_input = [[102,157], [-146,-90]]

INPUT = puzzle_input

min_x = INPUT[0][0]
max_x = INPUT[0][1]
min_y = INPUT[1][0]
max_y = INPUT[1][1]

def find_t_in_target(Vy):
    highest = 0
    yt = 0
    for t in range(1, 999):
        yt = yt + (Vy - t + 1)
        # print(f"{Vy} -- y({t})={yt}")
        if yt > highest:
            highest = yt
        if min_y <= yt and yt <= max_y:
            return (t, highest)
        if yt < min_y:
            return (None, highest)

# find the min vx that ends in target's x range
for min_vx in range(1, min_x):
    vx = min_vx
    xt = 0
    t= 0
    while vx > 0:
        xt += vx
        vx -=1
    if xt >= min_x:
        break

print(f"min_vx is {min_vx}")

def count_x_in_target(Vy, t_target):
    counter = 0
    for Vx in range(min_vx, max_x+1):
        xt = 0
        yt = 0
        Vxt = Vx
        for t in range(1, t_target*2):
            yt = yt + (Vy - t + 1)
            xt += Vxt
            # print(f"x(t{t})={xt} y(t{t})={yt}")
            Vxt = max(0, Vxt-1)
            if min_x <= xt and xt <= max_x and min_y <= yt and yt <= max_y:
                # print(f"------- valid velocity: {Vx}, {Vy}")
                counter += 1
                break
            if xt > max_x or yt < min_y:
                # print(f"xxxx too low")
                break
    return counter

highest_ever = 0
velocities = 0
for Vy in range(min_y, -min_y):
    t, top = find_t_in_target(Vy)
    if t is not None:
        # print(t, top)
        # phase 2:
        velocities += count_x_in_target(Vy, t)
        if top > highest_ever:
            highest_ever = top
            print(f"highest_ever = {highest_ever}")

print(f"{velocities} possibilities")

#phase 1: 
# puzzle highest_ever = 10585
# test highest_ever = 45

# phase 2
# test: 112 possibilities
# puzzle: 5247 possibilities
