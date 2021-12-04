input_test = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""

class Bingo:
    def __init__(self, line_generator):
        self.marks = []
        self.grid = []
        for i in range(5):
            self.marks.append([False] * 5)
            self.grid.append([0] * 5)
        for i in range(5):
            line = next(line_generator)
            if not line:
                line = next(line_generator)
            j = 0
            for number in line.split():
                if number:
                    self.grid[i][j] = int(number)
                    j += 1
            if j != 5:
                raise ValueError(f"can't load {line}")

    def mark(self):
        pass
    
    def is_winning(self):
        return False

    def __str__(self):
        return "\n".join((str(i) for i in self.grid))

lines = iter(input_test.split("\n"))

first_line = next(lines)
picked = [int(i) for i in first_line.split(",")]

grids = []
while True:
    try:
        grids.append(Bingo(lines))
    except StopIteration:
        break

print(f"loaded {len(grids)} grids")

