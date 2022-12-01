from collections import defaultdict

test_input = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""

puzzle_input = """PSVVKKCNBPNBBHNSFKBO

CF -> H
PP -> H
SP -> V
NO -> C
SF -> F
FS -> H
OF -> P
PN -> B
SH -> V
BO -> K
ON -> V
VP -> S
HN -> B
PS -> P
FV -> H
NC -> N
FN -> S
PF -> F
BF -> F
NB -> O
HS -> C
SC -> V
PC -> K
KF -> K
HC -> C
OK -> H
KS -> P
VF -> C
NV -> S
KK -> F
HV -> H
SV -> V
KC -> N
HF -> P
SN -> F
VS -> P
VN -> F
VH -> C
OB -> K
VV -> O
VC -> O
KP -> V
OP -> C
HO -> S
NP -> K
HB -> C
CS -> S
OO -> S
CV -> K
BS -> F
BH -> P
HP -> P
PK -> B
BB -> H
PV -> N
VO -> P
SS -> B
CC -> F
BC -> V
FF -> S
HK -> V
OH -> N
BV -> C
CP -> F
KN -> K
NN -> S
FB -> F
PH -> O
FH -> N
FK -> P
CK -> V
CN -> S
BP -> K
CH -> F
FP -> K
HH -> N
NF -> C
VB -> B
FO -> N
PB -> C
KH -> K
PO -> K
OV -> F
NH -> H
KV -> B
OS -> K
OC -> K
FC -> H
SO -> H
KO -> P
NS -> F
CB -> C
CO -> F
KB -> V
BK -> K
NK -> O
SK -> C
SB -> B
VK -> O
BN -> H"""

lines = iter(puzzle_input.split("\n"))

template = [c for c in next(lines).strip()]
_ = next(lines)

rules = dict(line.split(" -> ") for line in lines)

def step(chain):
    i = 1
    while i < len(chain):
        pair = chain[i-1] + chain[i]
        if pair in rules:
            chain.insert(i, rules[pair])
            i += 1
        i += 1

def phase1():
    tmpl = template[:]
    for i in range(10):
        step(tmpl)
        print(f"step {i+1}, {len(tmpl)} items")

    print("length: ", len(tmpl))

    counts = defaultdict(int)
    for i in tmpl:
        counts[i] += 1

    counts = list(counts.items())
    counts.sort(key=lambda t: t[1])
    print(counts)
    print(counts[-1][1] - counts[0][1])

phase1()

################# PHASE 1 ##########################
"""
on puzzle 
step 10, 19457 items
[('O', 514), ('V', 1222), ('N', 1491), ('B', 1492), ('S', 1699), ('C', 2181), ('P', 2201), ('K', 2467), ('H', 3092), ('F', 3098)]
most-least frequent = 2584

on test
step 10, 3073 items
[('H', 161), ('C', 298), ('N', 865), ('B', 1749)]
most-least frequent = 1588
"""

letters = set(template)
for pair,letter in rules.items():
    letters.add(letter)

pairs = {}
counts = {}
for l1 in letters:
    counts[l1] = 0
    for l2 in letters:
        pairs[l1+l2] = 0
for i in range(1, len(template)):
    pairs[template[i-1] + template[i]] += 1
    counts[template[i]] += 1
counts[template[0]] += 1

for step in range(40):
    pairs_after = dict(pairs)
    for pair,letter in rules.items():
        pairs_after[pair] -= pairs[pair]
        pairs_after[pair[0]+letter] += pairs[pair]
        pairs_after[letter+pair[1]] += pairs[pair]
        counts[letter] += pairs[pair]
    pairs = pairs_after

counts = list(counts.items())
counts.sort(key=lambda t: t[1])
print(counts)
print(counts[-1][1] - counts[0][1])
