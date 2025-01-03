from collections import defaultdict

lines = open("day5_input.txt").readlines()

instructions_start_at = 1

def find_stack_indexes():
    global instructions_start_at
    instructions_start_at = 1 # re-init, it's called 2 times
    indexes = {}
    for line in lines:
        instructions_start_at += 1
        if '[' in line:
            continue
        for (i, character) in enumerate(line):
            if character == ' ' or character == '\n':
                continue
            indexes[character] = i
        return indexes

def parse_stacks():
    indexes = find_stack_indexes()
    stacks = defaultdict(list)
    for line in lines:
        if '[' in line:
            for stack in indexes:
                char_at_column = line[indexes[stack]]
                if char_at_column != ' ':
                    stacks[stack].insert(0, char_at_column)
        else:
            return stacks

stacks9000 = parse_stacks()
stacks9001 = parse_stacks()

for i in range(instructions_start_at, len(lines)):
    instruction = lines[i].split()
    times = int(instruction[1])
    source = instruction[3]
    dest = instruction[5]
    stacks9001[dest] = stacks9001[dest] + stacks9001[source][-times:]
    for j in range(times):
        stacks9000[dest].append(stacks9000[source].pop())
        stacks9001[source].pop()

stack_keys = list(stacks9000.keys())
stack_keys.sort()
skyline9000 = ''
skyline9001 = ''
for k in stack_keys:
    if stacks9000[k]:
        skyline9000 += stacks9000[k][-1]
    if stacks9001[k]:
        skyline9001 += stacks9001[k][-1]

print(f"createMover9000 : {skyline9000}")
print(f"createMover9001 : {skyline9001}")


