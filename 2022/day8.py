from __future__ import annotations
lines = open("day8_input.txt").readlines()

trees = list()
for line in lines:
    row = list()
    for c in line.strip():
        row.append(int(c))
    trees.append(row)

visible_trees = set()

for i in range(len(trees)):
    horizon = -1
    for j in range(len(trees[i])):
        if trees[i][j] > horizon:
            visible_trees.add((i, j))
            horizon = trees[i][j]
            if horizon == 9:
                break

for i in range(len(trees)):
    horizon = -1
    for j in range(len(trees[i])-1 ,-1 ,-1):
        if trees[i][j] > horizon:
            visible_trees.add((i, j))
            horizon = trees[i][j]
            if horizon == 9:
                break

for i in range(len(trees[0])):
    horizon = -1
    for j in range(len(trees)):
        if trees[j][i] > horizon:
            visible_trees.add((j, i))
            horizon = trees[j][i]
            if horizon == 9:
                break

for i in range(len(trees[0])):
    horizon = -1
    for j in range(len(trees)-1, -1, -1):
        if trees[j][i] > horizon:
            visible_trees.add((j, i))
            horizon = trees[j][i]
            if horizon == 9:
                break

print(f"visible trees from outside (part1) : {len(visible_trees)}")

def scenic_score(i, j):
    global trees
    highest = trees[i][j]
    up_distance = 0
    for k in range(i-1, -1, -1):
        up_distance += 1
        if trees[k][j] >= highest:
            break

    down_distance = 0
    for k in range(i+1, len(trees)):
        down_distance += 1
        if trees[k][j] >= highest:
            break

    right_distance = 0
    for k in range(j+1, len(trees[0])):
        right_distance += 1
        if trees[i][k] >= highest:
            break

    left_distance = 0
    for k in range(j-1, -1, -1):
        left_distance += 1
        if trees[i][k] >= highest:
            break

    return up_distance * down_distance * right_distance * left_distance

best = 0
# edge score is always 0
for i in range(1, len(trees)-1):
    for j in range(1, len(trees[0])-1):
        best = max(best, scenic_score(i, j))

print(f"best scenic score = {best}")
