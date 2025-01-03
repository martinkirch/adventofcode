from functools import total_ordering
lines = open("day13_input.txt").readlines()

@total_ordering
class Packet:
    def __init__(self, wrapped):
        self.l = wrapped

    def __eq__(self, __o: object) -> bool:
        return (isinstance(__o, Packet)
            and Packet.correct(self.l, __o.l) == 0
        )

    def __lt__(self, __o: object) -> bool:
        return (isinstance(__o, Packet)
            and Packet.correct(self.l, __o.l) < 0
        )

    def correct(left, right):
        match (left, right):
            case (int(), int()):
                if left < right:
                    return -1
                elif left > right:
                    return 1
                else:
                    return 0
            case (list(), list()):
                i = 0
                j = 0
                while True:
                    if i == len(left) and j == len(right):
                        return 0
                    elif i == len(left):
                        return -1
                    elif j == len(right):
                        return 1
                    else:
                        classified = Packet.correct(left[i], right[j])
                        if classified != 0:
                            return classified
                    i += 1
                    j += 1
            case (int(), list()):
                return Packet.correct([left], right)
            case (list(), int()):
                return Packet.correct(left, [right])
            case _:
                raise ValueError("Ahem ahem")

pairs = []
flat = []
left = None
right = None
for line in lines:
    if line == '\n':
        pass
    elif left is None:
        left = eval(line)
        flat.append(Packet(left))
    else:
        right = eval(line)
        flat.append(Packet(right))
        pairs.append((left, right))
        left = None
flat.append(Packet([[2]]))
flat.append(Packet([[6]]))

correct_indices_sum = 0
for i, pair in enumerate(pairs):
    index = i+1
    if Packet.correct(pair[0], pair[1]) == -1:
        #print(f"pair #{index} {pair[0], pair[1]} is correct")
        correct_indices_sum += index

# 5252
print(f"Sum of correct indices: {correct_indices_sum}")

flat.sort()
print("sorted")

divider1 = flat.index(Packet([[2]])) + 1
divider2 = flat.index(Packet([[6]])) + 1

print(f"decoder key = {divider1 * divider2}")
