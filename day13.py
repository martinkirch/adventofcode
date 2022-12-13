from typing import Tuple, List
lines = open("day13_test.txt").readlines()

pairs = []
left = None
right = None
for line in lines:
    if line == '\n':
        pass
    elif left is None:
        left = eval(line)
    else:
        right = eval(line)
        pairs.append((left, right))
        left = None

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
                    classified = correct(left[i], right[j])
                    if classified != 0:
                        return classified
                i += 1
                j += 1
        case (int(), list()):
            return correct([left], right)
        case (list(), int()):
            return correct(left, [right])
        case _:
            raise ValueError("Ahem ahem")

correct_indices_sum = 0
for i, pair in enumerate(pairs):
    index = i+1
    if correct(pair[0], pair[1]) == -1:
        print(f"pair #{index} {pair[0], pair[1]} is correct")
        correct_indices_sum += index

# 5252
print(f"Sum of correct indices: {correct_indices_sum}")
