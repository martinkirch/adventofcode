import re
from collections import defaultdict

test_input = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""

larger_input = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""

even_larger_input = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""

puzzle_input = """rf-RL
rf-wz
wz-RL
AV-mh
end-wz
end-dm
wz-gy
wz-dm
cg-AV
rf-AV
rf-gy
end-mh
cg-gy
cg-RL
gy-RL
VI-gy
AV-gy
dm-rf
start-cg
start-RL
rf-mh
AV-start
qk-mh
wz-mh"""

ISUPPER = re.compile("[A-Z]+")
def isupper(s):
    return ISUPPER.match(s)

INPUT = puzzle_input

connections = defaultdict(list)
connections["end"] = []

for line in INPUT.split("\n"):
    caves = line.split("-")
    caves.sort(key=len)
    if caves[1] == "start":
        connections["start"].append(caves[0])
    elif caves[1] == "end":
        connections[caves[0]].append("end")
    else:
        connections[caves[0]].append(caves[1])
        connections[caves[1]].append(caves[0])

nbpaths = 0
path = []
def start(cave):
    path.append(cave)
    possible_next = [c for c in connections[cave] if isupper(c) or c not in path]
    total = 0
    if possible_next:
        for n in possible_next:
            total += start(n)
    else:
        if cave == "end":
            total = 1
    path.pop()
    return total

print(start("start"))
