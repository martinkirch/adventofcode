"""
Day 18: Snailfish
"""
from copy import deepcopy

test_input = """[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]"""

puzzle_input = """[[1,[8,[5,8]]],[[4,4],[8,[8,8]]]]
[[[3,[2,3]],[[8,0],2]],[0,[[8,1],[7,0]]]]
[4,[[0,3],[[6,6],[3,8]]]]
[[[7,[6,4]],[[0,6],[2,0]]],[[[5,6],[0,4]],[[8,1],[9,1]]]]
[[[6,3],[[6,9],4]],[[1,[4,2]],[[0,0],1]]]
[[2,0],[3,[0,8]]]
[[0,[5,5]],[[4,2],[3,[6,4]]]]
[[[[9,9],[8,5]],[7,4]],[[6,9],[8,[0,8]]]]
[[[[7,1],[2,9]],[[9,3],0]],[3,[[0,6],[7,6]]]]
[[[[3,7],[7,1]],[[5,8],[0,1]]],3]
[[[[4,6],[6,2]],[[9,1],7]],[[9,1],[8,0]]]
[[[[2,7],0],[[9,4],[2,6]]],[0,[[7,4],[0,3]]]]
[[5,[[0,2],[8,8]]],[[[4,1],9],3]]
[[[7,1],[[3,7],[3,4]]],[[[0,7],[1,6]],1]]
[[[6,5],[[1,8],[8,8]]],[[4,5],[3,7]]]
[[[1,[3,3]],[[3,2],[5,7]]],[[8,[9,3]],[[5,3],4]]]
[[[4,[2,7]],9],[9,[[5,6],4]]]
[[[9,1],3],[[1,2],9]]
[[[[0,0],[2,3]],[[7,8],[1,5]]],[[[8,6],7],[[8,3],9]]]
[6,[[5,[0,8]],1]]
[4,[[[3,0],[2,0]],[[7,2],[1,4]]]]
[[[[4,3],[4,1]],8],[[[9,4],[1,9]],[4,[0,6]]]]
[4,[5,6]]
[[[0,[6,1]],[[6,1],3]],[[0,[7,8]],[1,0]]]
[[5,[[8,7],8]],8]
[[5,[[5,2],0]],[[1,[4,7]],[[0,9],[2,3]]]]
[[7,[2,2]],[[6,3],[5,8]]]
[[[0,9],5],[1,[[5,7],1]]]
[[8,[3,[0,3]]],[[[2,2],2],[[8,8],[8,9]]]]
[[6,[[3,2],[2,6]]],[5,1]]
[[[[9,8],[6,8]],[0,7]],7]
[[[7,2],[[6,3],4]],2]
[[[5,2],[[1,6],[8,3]]],[6,5]]
[[5,2],[0,5]]
[[[[4,5],5],[[4,6],[1,2]]],[[[3,6],[4,9]],[1,9]]]
[[1,[4,1]],[[9,[5,5]],[[9,0],[5,7]]]]
[[[[8,9],[7,7]],2],[8,1]]
[[[8,1],[8,[9,5]]],3]
[[[2,[3,9]],[[5,4],[7,9]]],[9,8]]
[8,[[2,[0,9]],[[5,0],4]]]
[[[6,[4,8]],[0,6]],[[8,[1,8]],1]]
[[6,[[1,0],[6,2]]],[[9,[3,7]],[5,[4,0]]]]
[[8,[0,[9,1]]],8]
[7,[4,[7,2]]]
[[1,[[5,7],[5,4]]],[[5,[8,0]],[1,6]]]
[[[[0,6],[6,2]],3],[[[9,3],7],[7,[1,2]]]]
[[[6,[4,9]],8],[6,5]]
[[[0,[1,9]],[[1,9],[3,9]]],[[[3,4],[7,5]],3]]
[[[[9,3],5],[[0,5],[2,7]]],9]
[[[6,[7,5]],5],[1,[[7,0],[3,4]]]]
[[[2,1],[[1,3],[1,5]]],[4,[9,[7,9]]]]
[[[[7,9],4],[[8,8],7]],[[[3,5],2],[[4,4],[6,5]]]]
[[1,1],[1,1]]
[[8,[0,2]],8]
[[[2,[2,1]],[[1,7],[1,2]]],[[1,6],5]]
[6,[0,[[1,0],[0,9]]]]
[6,[[2,[8,0]],[8,[8,8]]]]
[4,[[3,[0,3]],4]]
[[[5,3],3],[[0,[7,6]],[2,[5,8]]]]
[[[[8,1],[4,1]],[[5,8],[4,8]]],[[[1,7],[7,2]],[0,[2,7]]]]
[[[2,[3,5]],3],5]
[[7,[[9,5],[8,2]]],[[[1,8],8],5]]
[[3,5],[[4,[9,3]],5]]
[[[[4,6],2],[2,2]],[0,[0,4]]]
[[[[5,8],[6,6]],[2,0]],[[[2,3],9],[[4,5],2]]]
[[[[1,9],3],[[3,4],6]],[[3,6],[6,[0,7]]]]
[[[0,[5,5]],[2,6]],[[[7,4],4],2]]
[0,[[8,[6,2]],[5,[1,5]]]]
[[[[5,5],[9,6]],[[5,2],2]],[[4,7],[[5,5],[1,6]]]]
[[4,7],[[[1,8],[9,6]],[2,3]]]
[5,[5,4]]
[[[[2,1],[7,0]],[5,[7,8]]],[6,[3,1]]]
[[[3,1],[[2,4],6]],[[[1,8],[2,1]],[[1,7],4]]]
[[[5,[3,3]],6],[[[0,0],9],[1,[7,4]]]]
[[[6,5],[[7,3],4]],[[9,[0,3]],[3,[6,0]]]]
[[[3,4],7],[8,[[1,7],[9,9]]]]
[[[[2,1],6],[2,6]],[[[8,1],[6,2]],[9,0]]]
[[8,4],[5,2]]
[[4,[[4,5],9]],[[3,[5,2]],[4,2]]]
[[[8,8],[[8,0],[5,3]]],4]
[[1,8],[0,2]]
[[[[7,2],[9,0]],[[9,2],[1,2]]],[[[4,0],3],0]]
[[[[1,2],[1,8]],[[4,3],[8,6]]],[[[5,1],8],[8,1]]]
[[[[5,3],[7,2]],7],[[6,[7,9]],[[3,8],[9,4]]]]
[[[[3,1],[2,5]],6],[[[3,2],[8,8]],[4,6]]]
[9,[[3,[2,3]],6]]
[[[[4,0],[5,6]],[5,4]],[[[9,0],[1,8]],[5,[3,6]]]]
[[[[9,5],[9,4]],[[5,7],5]],[[[1,4],7],[6,1]]]
[[2,[6,[8,2]]],[7,[1,[3,3]]]]
[[[9,1],[0,[6,3]]],[[5,[1,5]],[7,[1,0]]]]
[1,6]
[[0,[2,[8,9]]],[[[4,5],[5,4]],1]]
[[[1,[4,1]],8],[[2,[7,0]],[7,[9,9]]]]
[[[[5,7],[3,5]],[[6,6],2]],[2,[8,[9,0]]]]
[6,[[[3,9],8],[[4,3],[6,1]]]]
[[[[6,7],[7,6]],[2,8]],[[9,[4,1]],6]]
[[[[4,5],[4,5]],[[0,6],5]],[[[6,5],[7,0]],1]]
[[[[6,7],9],[[5,5],[6,6]]],[[7,1],[[8,2],[3,1]]]]
[[[9,6],7],[[[1,8],8],[1,7]]]
[[5,2],[[1,9],[2,2]]]"""

INPUT = test_input

numbers = [eval(l) for l in INPUT.split("\n")]

class Explosion(Exception):
    def __init__(self, pair):
        self.left = pair[0]
        self.right = pair[1]
        #print(self)

    def __str__(self):
        return(f"Explosion([{self.left}, {self.right}]")

class Splitted(Exception):
    pass

def increment_side(idx, liste, value):
    if isinstance(liste[idx], int):
        liste[idx] += value
    else:
        increment_side(idx, liste[idx], value)

def split(value):
    splitted = [value // 2, value // 2 + value % 2]
    #print(f"Splitted as {splitted}")
    return splitted

def explose_step(pair, depth=0):
    if isinstance(pair, list):
        if depth == 4:
            raise Explosion(pair)
        else:
            try:
                explose_step(pair[0], depth=depth+1)
            except Explosion as exp:
                if exp.right is not None and exp.left is not None:
                    pair[0] = 0
                if exp.right is not None:
                    if isinstance(pair[1], int):
                        pair[1] += exp.right
                    else:
                        increment_side(0, pair[1], exp.right)
                    exp.right = None
                raise
            try:
                explose_step(pair[1], depth=depth+1)
            except Explosion as exp:
                if exp.right is not None and exp.left is not None:
                    pair[1] = 0
                if exp.left is not None:
                    if isinstance(pair[0], int):
                        pair[0] += exp.left
                    else:
                        increment_side(1, pair[0], exp.left)
                    exp.left = None
                raise

def split_step(pair):
    if isinstance(pair, list):
        try:
            split_step(pair[0])
            if isinstance(pair[0], int) and pair[0] >= 10:
                pair[0] = split(pair[0])
                raise Splitted()
            split_step(pair[1])
            if isinstance(pair[1], int) and pair[1] >= 10:
                pair[1] = split(pair[1])
                raise Splitted()
        except Splitted:
            raise

def reduce_loop(added):
    try_again = True
    while try_again:
        try_again = False
        try:
            #print(added)
            explose_step(added)
            split_step(added)
        except (Explosion, Splitted) as exn:
            try_again = True

number = deepcopy(numbers[0])
for i in range(1, len(numbers)):
    number = [number, deepcopy(numbers[i])]
    reduce_loop(number)
print(number)

def magnitude(pair):
    if isinstance(pair, list):
        return 3 * magnitude(pair[0]) + 2 * magnitude(pair[1])
    else:
        return pair
print(f"magnitude is {magnitude(number)}")

# phase1: 
# test_input magnitude is 4140
# puzzle_input magnitude is 3524


greatest_magnitude = 0
greatest_magnitude_pair = None
for i in range(len(numbers)):
    for j in range(len(numbers)):
        if i != j:
            number = [deepcopy(numbers[i]), deepcopy(numbers[j])]
            reduce_loop(number)
            mag = magnitude(number)
            if mag > greatest_magnitude:
                greatest_magnitude = mag
                greatest_magnitude_pair = (i, j)

# phase 2:
print(f"Greatest magnitude is {greatest_magnitude} (couple {greatest_magnitude_pair})")
print(f"Obtained by\n{numbers[greatest_magnitude_pair[0]]}")
print(f"+\n{numbers[greatest_magnitude_pair[1]]}")

"""
test:
Greatest magnitude is 3993 (couple (8, 0))
Obtained by
[[2, [[7, 7], 7]], [[5, 8], [[9, 3], [0, 2]]]]
+
[[[0, [5, 8]], [[1, 7], [9, 6]]], [[4, [1, 2]], [[1, 4], 2]]]


puzzle: 
Greatest magnitude is 4656 (couple (97, 51))
Obtained by
[[[[6, 7], 9], [[5, 5], [6, 6]]], [[7, 1], [[8, 2], [3, 1]]]]
+
[[[[7, 9], 4], [[8, 8], 7]], [[[3, 5], 2], [[4, 4], [6, 5]]]]

"""
