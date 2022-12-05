lines = open("day3_input.txt").readlines()

ORD_a = ord('a')
ORD_A = ord('A')

def priority(item):
    priority = ord(item)
    if priority >= ORD_a:
        return priority - ORD_a + 1
    else:
        return priority - ORD_A + 27

#print(f'p={priority("p")} P={priority("P")} L={priority("L")} Z={priority("Z")} ')

total_priority = 0

for line in lines:
    line = line.strip()
    if line:
        first = set(line[0:len(line)//2])
        common = first.intersection(line[len(line)//2:])
        for i in common:
            total_priority += priority(i)

print(f"total priorities: {total_priority}")

total_badges_priorities = 0
for i in range(0, len(lines), 3):
    common = set(lines[i].strip())
    common = common.intersection(lines[i+1].strip())
    common = common.intersection(lines[i+2].strip())
    assert len(common) == 1
    total_badges_priorities += priority(common.pop())

print(f"total badges' priorities = {total_badges_priorities}")
