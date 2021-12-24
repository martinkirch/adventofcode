"""
Day 18: Snailfish
"""

test_input = """[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
[7,[5,[[3,8],[1,4]]]]
[[2,[2,2]],[8,[8,1]]]
[2,9]
[1,[[[9,3],9],[[9,0],[0,7]]]]
[[[5,[7,4]],7],1]
[[[[4,2],2],6],[8,7]]"""

test_input = """[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]"""
INPUT = test_input

numbers = [eval(l) for l in INPUT.split("\n")]

class Explosion(Exception):
    def __init__(self, pair):
        self.left = pair[0]
        self.right = pair[1]
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
    return [value // 2, value // 2 + value % 2]

def reduce_step(pair, depth=0):
    if isinstance(pair, list):
        if depth == 4:
            raise Explosion(pair)
        else:
            try:
                reduce_step(pair[0], depth=depth+1)
            except Splitted:
                raise
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
                reduce_step(pair[1], depth=depth+1)
            except Splitted:
                raise
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
            if isinstance(pair[0], int) and pair[0] >= 10:
                pair[0] = split(pair[0])
                raise Splitted()
            if isinstance(pair[1], int) and pair[1] >= 10:
                pair[1] = split(pair[1])
                raise Splitted()

number = numbers[0]
for i in range(1, len(numbers)):
    number = [number, numbers[i]]
    try_again = True
    while try_again:
        try_again = False
        try:
            print(number)
            reduce_step(number)
        except (Explosion, Splitted) as exn:
            print(exn)
            try_again = True
print(number)
