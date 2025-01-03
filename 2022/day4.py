lines = open("day4_input.txt").readlines()

fully_contained = 0
overlap = 0

for line in lines:
    pair = line.strip().split(',')
    left = [int(i) for i in pair[0].split('-')]
    right = [int(i) for i in pair[1].split('-')]
    if ((left[0] <= right[0] and right[1] <= left[1]) or
        (right[0] <= left[0] and left[1] <= right[1])
    ):
        fully_contained += 1
    if not ((left[1] < right[0]) or (right[1] < left[0])):
        overlap += 1

print(f"{fully_contained} pairs are fully contained in one another")
print(f"{overlap} pairs overlap")
