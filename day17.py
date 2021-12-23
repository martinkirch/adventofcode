"""
Day17 "trick shot"

y0 and x0 are 0

x(t) = x(t_prev) + max(Vx - t, 0) 
y(t) = y(t_prev) + Vy - t + 1

"""
from math import sqrt

test_input = [[20,30],[-10,-5]]
puzzle_input = [[102,157], [-146,-90]]

INPUT = test_input

min_x = INPUT[0][0]
max_x = INPUT[0][1]
min_y = INPUT[1][0]
max_y = INPUT[1][1]

def find_t_in_target(Vy):
    highest = 0
    yt = 0
    for t in range(1, 999):
        yt = yt + (Vy - t + 1)
        print(f"{Vy} -- y({t})={yt}")
        if yt > highest:
            highest = yt
        if min_y <= yt and yt <= max_y:
            return (t, highest)
        if yt < min_y:
            return (None, highest)

highest_ever = 0
for Vy in range(-min_y):
    t, top = find_t_in_target(Vy)
    if t is not None:
        print(t, top)
        if top > highest_ever:
            highest_ever = top
            print(f"highest_ever = {highest_ever}")

#phase 1: 
# puzzle highest_ever = 10585
# test highest_ever = 45
