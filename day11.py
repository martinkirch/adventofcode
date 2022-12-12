from __future__ import annotations
lines = open("day11_input.txt").readlines()

class Monkey:
    def __init__(self, lines:list[str]):
        self.inspected = 0
        self.index = int(lines[0][7:-2])
        self.items = [int(i) for i in lines[1][18:-1].split(",")]
        self.operation = lines[2][19:-1]
        self.test_divisible = int(lines[3][21:-1])
        self.dest_if_test = int(lines[4].split()[-1])
        self.dest_if_not_test = int(lines[5].split()[-1])
    
    def __str__(self):
        return f"""Monkey {self.index}:
        Items: {self.items}
        Operation: {self.operation}
        Test: divisible by {self.test_divisible}
           if true: give to monkey {self.dest_if_test}
           if false: give to monkey {self.dest_if_not_test}
        """
    
    def turn(self):
        global monkeys
        while self.items:
            self.inspected += 1
            old = self.items.pop(0)
            worry = eval(self.operation)
            worry = worry // 3
            if (worry % self.test_divisible) == 0:
                monkeys[self.dest_if_test].items.append(worry)
            else:
                monkeys[self.dest_if_not_test].items.append(worry)

monkeys:list[Monkey] = list()
i=0
while i < len(lines):
    monkeys.append(Monkey(lines[i:i+7]))
    i += 7

for round in range(20):
    # print(f"\n== After round {round}")
    for monkey in monkeys:
        monkey.turn()
    # for monkey in monkeys:
    #     print(f"Monkey {monkey.index} holds {monkey.items}")
    # for monkey in monkeys:
    #     print(f"Monkey {monkey.index} inspected items {monkey.inspected} times")

inspections = [m.inspected for m in monkeys]
inspections.sort(reverse=True)
print(inspections[0]*inspections[1])
