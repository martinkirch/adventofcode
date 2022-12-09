lines = open("day9_input.txt").readlines()

H = (0, 0)
T = (0, 0)
traversed = set()

directions = {
    'R': lambda pos: (pos[0], pos[1] + 1),
    'U': lambda pos: (pos[0] + 1, pos[1]),
    'L': lambda pos: (pos[0], pos[1] - 1),
    'D': lambda pos: (pos[0] - 1, pos[1]),
}

for line in lines:
    splitted = line.strip().split()
    times = int(splitted[1])
    for i in range(times):
        H = directions[splitted[0]](H)
        if abs(H[0] - T[0]) <= 1 and abs(H[1] - T[1]) <= 1:
            pass # no need to move !
        elif abs(H[0] - T[0]) == 2:
            if H[0] > T[0]:
                T = (H[0] - 1, H[1])
            else:
                T = (H[0] + 1, H[1])
        elif abs(H[1] - T[1]) == 2:
            if H[1] > T[1]:
                T = (H[0], H[1] - 1)
            else:
                T = (H[0], H[1] + 1)
        else:
            ValueError("That's unexpected")
        traversed.add(T)

print(len(traversed))

rope = [(0,0)]*10
traversed = set()
for line in lines:
    splitted = line.strip().split()
    times = int(splitted[1])
    for i in range(times):
        rope[0] = directions[splitted[0]](rope[0])
        H = rope[0]
        for node in range(1, len(rope)):
            T = rope[node]
            if abs(H[0] - T[0]) <= 1 and abs(H[1] - T[1]) <= 1:
                pass # no need to move !
            elif abs(H[0] - T[0]) == 2 and abs(H[1] - T[1]) == 2:
                if H[0] > T[0]:
                    t0 = H[0] - 1
                else:
                    t0 = H[0] + 1
                if H[1] > T[1]:
                    t1 = H[1] - 1
                else:
                    t1 = H[1] + 1
                T = (t0, t1)
            elif abs(H[0] - T[0]) == 2:
                if H[0] > T[0]:
                    T = (H[0] - 1, H[1])
                else:
                    T = (H[0] + 1, H[1])
            elif abs(H[1] - T[1]) == 2:
                if H[1] > T[1]:
                    T = (H[0], H[1] - 1)
                else:
                    T = (H[0], H[1] + 1)
            else:
                ValueError("That's unexpected")
            rope[node] = T
            H = T
        traversed.add(T)

# 2235 too low !
print(len(traversed))

